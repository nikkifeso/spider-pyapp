import unittest
from src.db.pages import Pages
from src.db import DB


class MyTestPages(unittest.TestCase):
  """
  This class tests the various methods available to the Pages class.
  """
  def setUp(self) -> None:
     self.DB = Pages(DB.connect())

  def test_select(self):
    self.DB.select()
    self.assertIsNotNone(self.DB.select())

  def fetch(self):
    self.DB.fetch(2)
    self.assertIsNotNone(self.DB.fetch(2))

  def update(self):
    self.DB.update(True, 1)
    self.assertIsNotNone(self.DB.update(True, 1))

  def tearDown(self) -> None:
     self.DB = None


if __name__ == '__main__':
  unittest.main()
