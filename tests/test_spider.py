import unittest
from src.spider import scraping_function


class TestSpider(unittest.TestCase):
  """
  This class tests the scraping function.
  """

  def test_scraping_raises_exception(self):
    """
    Tests that an exception is raised for wrong ids.
    """
    with self.assertRaises(TypeError):
      self.assertEqual(scraping_function(3), None)


if __name__ == '__main__':
  unittest.main()
