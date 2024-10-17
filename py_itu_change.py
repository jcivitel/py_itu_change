import asyncio
import os
import sys
from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup
from tabulate import tabulate


def progress_bar(iteration, total):
    """
    :description:
    function to generate a progress bar
    :param iteration:
    :param total:
    """

    # Get terminal width dynamically
    terminal_width = os.get_terminal_size().columns
    # Reserve some space for text (e.g., 'Progress: | ... | 100.00%')
    reserved_space = 20
    length = terminal_width - reserved_space

    percent = 100 * (iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = "#" * filled_length + "-" * (length - filled_length)

    sys.stdout.write(f"\rProgress: |\033[92m{bar}\033[0m| {percent:.2f}%")
    sys.stdout.flush()


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
    """
    function to process each country and get the latest update timestamp
    :param session:
    :param value:
    :param filter_date:
    :return: None
    """
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
        if update_date > filter_date:
            return [country.text.strip(), update_date, link]
    return None


async def main():
    """
    :description: The Main function of the program
    :param filter_date: the first argument should be the date in `YYYY-MM-DD` format
    :return: True
    """
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

        total_tasks = len(tasks)
        completed_tasks = 0

        progress_bar(completed_tasks, total_tasks)

        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result:
                results.append(result)
                print(f"\33[2K\rCountry: {result[0]}, Update Date: {result[1]}")

            completed_tasks += 1
            progress_bar(completed_tasks, total_tasks)

        data_list = [result for result in results if result]
        data_list.sort(key=lambda x: x[1])

    country_updated = len(data_list)
    sys.stdout.write("\n")
    """print the result list"""
    if len(data_list) >= 2:
        print("\n\n")
        print(
            tabulate(data_list, headers=["Country", "Date", "Link"], tablefmt="github")
        )

    print(f"\n\033[93m{country_updated} countries have new updates")


"""
check if to call the main function
"""
if __name__ == "__main__":
    asyncio.run(main())
