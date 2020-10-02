import requests
from bs4 import BeautifulSoup
from src.db import DB


def scraping_function(id):
  """
  This function implements the web scraper that inserts into the liks table.
  :param
  id(int): The id at which the url to be scraped is retrieved.
  :return:
  None: Returns None
  :raises:
  TypeError: Raises a TypeError
  """
  try:
    # retrieves the url from the pages table
    url = DB.pages().fetch(id)
    DB.pages().update(True, id)

    link_list = []
    r = requests.get(url[0])
    # scrapes the url for hyperlinks
    soup = BeautifulSoup(r.text, features='html.parser')
    for link in soup.find_all('a', href=True):
      if 'https' in link['href']:
        link_list.append(link['href'])
    links = link_list[:10]
    DB.links().delete(id)
    for i in links:
      DB.links().insert(id, i)
    DB.pages().update(False, id)
    return None
  except TypeError:
    raise TypeError('Id not found in Pages Table')

