# Show examples of how you would use ALL your implementations here
from celery import Celery
from decouple import config
from src.spider import scraping_function
from src.db import DB
from src.db.pages import Pages

# ---Usage of Spider.py---
app = Celery('spider', broker=config('CELERY_BROKER'), backend=config('CELERY_BACKEND'))


@app.task()
def cel_spider():
  """
  Implements the celery task for the spider
  :return
  None: Returns the value of the scraping function.
  """
  return scraping_function(2)
#
#  ---- Usage of DB class ----
#
# DB.serv_conn()
# # # DB.connect()
# DB.setup()
# DB.seed()
#
# # ----Usage of pages.py----
# DB.pages().select()
# DB.pages().fetch(2)
# DB.pages().update(True, 2)
#
# # ----Usage of links.py----
# DB.links().select()
# DB.links().fetch()
# DB.links().insert(1, 'https://www.facebook.com')
DB.links().delete(1)

# scraping_function(3)