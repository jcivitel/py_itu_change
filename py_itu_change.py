import csv
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def check_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


url = "https://www.itu.int/oth/T0202.aspx?lang=en&parent=T0202"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

dropdown = soup.find("select", {"id": "ctl00_ContentPlaceHolder1_ctl01_lstCountryPrefix"})

data_list = [["Land", "Datum", "Link"]]

for option in dropdown.find_all("option"):
    value = option["value"]

    if value:
        link = f"https://www.itu.int/oth/{value}/en"

        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        posted_date = soup.find_all("b")
        country = soup.find("title")

        for i in range(8, 11):
            try:
                if check_date_format(posted_date[i].text.strip()):
                    update_date = posted_date[i].text.strip()
                    break
            except:
                continue

        if posted_date:
            print(f"Land: {country.text.strip()}, {update_date}")
            # Filter Dates
            if update_date > "2023-01-01":
                data_list.append([country.text.strip(), update_date, link])

today = datetime.today()

with open(f"ITU-Change-{today.strftime('%Y_%m_%d')}.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for row in data_list:
        writer.writerow(row)
