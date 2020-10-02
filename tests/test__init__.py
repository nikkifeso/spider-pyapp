import unittest
from src.db import DB


class MyTestCases(unittest.TestCase):
  """
  This class tests the various methods available to the DB class.
  """
  def setUp(self) -> None:
     self.DB = DB().serv_conn()

  def test_serv_conn(self):
    connection_object = self.DB
    self.assertIsNotNone(connection_object)

  def test_connect(self):
    connection_object = DB.connect()
    self.assertIsNotNone(connection_object)

  def test_setup(self):
    self.assertEqual(DB.setup(), None)

  def test_seed(self):
    self.assertEqual(DB.seed(), None)

  def test_links(self):
    self.assertIsNotNone(DB.links())

  def test_pages(self):
     self.assertIsNotNone(DB.pages())

  def tearDown(self) -> None:
     self.DB = None


if __name__ == '__main__':
  unittest.main()
