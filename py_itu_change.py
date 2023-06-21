from datetime import datetime

import requests
from bs4 import BeautifulSoup


def check_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# URL der Webseite mit dem Dropdown-Menü
url = "https://www.itu.int/oth/T0202.aspx?lang=en&parent=T0202#A"

# Webseite herunterladen
response = requests.get(url)

# BeautifulSoup verwenden, um die HTML-Daten zu analysieren
soup = BeautifulSoup(response.text, "html.parser")

# Das Dropdown-Menü finden
dropdown = soup.find("select", {"id": "ctl00_ContentPlaceHolder1_ctl01_lstCountryPrefix"})

# Alle Optionen im Dropdown-Menü durchgehen und den Link für jeden Wert öffnen
for option in dropdown.find_all("option"):
    value = option["value"]

    # Überprüfen, ob der Wert gültig ist (nicht leer)
    if value:
        # Den Link erstellen
        link = f"https://www.itu.int/oth/{value}/en"

        # Den Link öffnen und das "Posted" Datum auf der neuen Seite lesen
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        # Das "Posted" Datum finden und ausgeben
        posted_date = soup.find_all("b")
        country = soup.find("title")

        if check_date_format(posted_date[8].text.strip()):
            date = posted_date[8].text.strip()
        elif check_date_format(posted_date[9].text.strip()):
            date = posted_date[9].text.strip()
        elif check_date_format(posted_date[10].text.strip()):
            date = posted_date[10].text.strip()

        if posted_date:
            print(f"Land: {country.text.strip()}")
            print(f"Posted Datum: {date}")
            print("---")
