from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import logging

from pprint import pprint

load_dotenv()


def extract_edt(id_groupe: str = "I1 Groupe 4 Licence"):
    """Function to return the timetable of a group in 3iL

    Args:
        id_groupe (str, optional): Id of the group according to 3iL EDT. Defaults to "I2 Groupe 1".

    Returns:
        list: List up to date of the subjects availablen online
    """
    url = f"http://eleves.groupe3il.fr/edt_eleves/00_index.php?idGroupe={id_groupe}.xml"
    r = requests.get(url)
    if r.status_code != 200:
        logging.error("Unable to load the page")
        return []
    print(f"Fetching url: {url}")
    soup = BeautifulSoup(r.content, "html.parser")
    items = []
    for row in soup.select('div.edt-item'):
        item = dict()
        item['subject'] = row.select('div.activite-titre')[0].getText()
        item['room'] = row.select('div.edt-data')[1].getText()
        item['time'] = row.select('div')[1].getText()
        item['date'] = row.select('div')[3].getText()
        if (item['room'] != ''):
            items.append(item)

    return items


if __name__ == "__main__":
    items = extract_edt()
    pprint(items)
