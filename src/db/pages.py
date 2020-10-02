class Pages:
  def __init__(self, connect):
    self.cursor = connect.cursor()

  def select(self):
    """
    This function selects all from the pages table.
    :return:
    list: A list of all contents.
    """
    self.cursor.execute('SELECT * FROM pages')
    return self.cursor.fetchall()

  def fetch(self, id):
    """
    This function selects all urls from pages table at id.
    :param:
    url(string): The url from pages table
    id(int): The id at which url is selected.
    :return:
    list: A list containing first value of contents.
    """
    self.cursor.execute('SELECT url FROM pages WHERE id = %s', (id,))
    return self.cursor.fetchone()

  def update(self, value, id):
    """
    This function updates the pages table with value at id.
    :param
    value(Bool): True or False
    :param
    id(int): The id at which the value of is_scraping is updated.
    :return:
    list: A list of all contents in the table.
    """
    self.cursor.execute('UPDATE pages SET is_scraping = %s WHERE id = %s', (value, id))
    self.cursor.execute('SELECT * FROM pages')
    return self.cursor.fetchall()


