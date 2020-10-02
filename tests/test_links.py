import unittest
from src.db.links import Links
from src.db import DB


class MyTestLinks(unittest.TestCase):
  """
  This class tests the various methods available to the Links class.
  """
  def setUp(self) -> None:
    self.DB = Links(DB.connect())

  def test_select(self):
    self.assertIsNotNone(self.DB.select())

  def test_fetch(self):
    self.assertIsNotNone(self.DB.fetch())

  def test_insert(self):
    self.assertIsNotNone(self.DB.insert(2, 'https://rb.gy/zd2xxz'))

  def test_delete(self):
    self.assertIsNone(self.DB.delete(1))

  def tearDown(self) -> None:
    self.DB = None


if __name__ == '__main__':
  unittest.main()
