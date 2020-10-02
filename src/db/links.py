class Links:
  """
  This class contains the functions that executes SQL for the links table.
  """
  def __init__(self, connect):
    self.cursor = connect.cursor()

  def select(self):
    """
    This function selects all from the links table.
    :return:
    list: A list of all contents.
    """
    self.cursor.execute('SELECT * FROM links')
    return self.cursor.fetchall()

  def fetch(self):
    """
    This function selects all urls from links table.
    :return:
    list: A list containing all contents.
    """
    self.cursor.execute('SELECT url FROM links')
    return self.cursor.fetchall()

  def insert(self, page_id, url):
    """
    This function inserts values into the links table.
    :param
    page_id(int): This is the page_id to be inserted.
    :param
    url(string): This is the url to be inserted.
    :return
    list: A list containing all contents.
    """
    self.cursor.execute('INSERT INTO links (page_id, url) VALUES (%s, %s)', (page_id, url))
    self.cursor.execute('SELECT * FROM links')
    return self.cursor.fetchall()

  def delete(self, id):
    """
    This function deletes items in the links table.
    :param
    id(int): This is the id at which entries are deleted.
    :return:
    """
    self.cursor.execute('DELETE FROM links WHERE page_id = %s', (id,))


