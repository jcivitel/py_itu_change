import asyncio
import sys
from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup
from tabulate import tabulate


def check_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def process_country(session, value, filter_date):
    link = f"https://www.itu.int/oth/{value}/en"
    html = await fetch(session, link)
    soup = BeautifulSoup(html, "html.parser")

    posted_date = soup.find_all("b")
    country = soup.find("title")

    update_date = None
    for i in range(8, 11):
        try:
            if check_date_format(posted_date[i].text.strip()):
                update_date = posted_date[i].text.strip()
                break
        except:
            continue

    if update_date:
        print(f"Country: {country.text.strip()}, {update_date}", flush=True)
        if update_date > filter_date:
            return [country.text.strip(), update_date, link]
    return None


async def main():
    if len(sys.argv) <= 1:
        print("Please add the filter-date as param")
        return

    filter_date = sys.argv[1]
    url = "https://www.itu.int/oth/T0202.aspx?lang=en&parent=T0202"

    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, "html.parser")
        dropdown = soup.find(
            "select", {"id": "ctl00_ContentPlaceHolder1_ctl01_lstCountryPrefix"}
        )

        tasks = []
        for option in dropdown.find_all("option"):
            value = option.get("value")
            if value:
                tasks.append(process_country(session, value, filter_date))

        results = await asyncio.gather(*tasks)
        data_list = [result for result in results if result]
        data_list.sort(key=lambda x: x[1])

    country_updated = len(data_list)

    if len(data_list) >= 2:
        print("\n\n")
        print(
            tabulate(data_list, headers=["Country", "Date", "Link"], tablefmt="github")
        )

    print(f"\n{country_updated} countries have new updates")


if __name__ == "__main__":
    asyncio.run(main())
