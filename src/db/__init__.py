import psycopg2
from decouple import config
from src.db.pages import Pages
from src.db.links import Links


class DB:
  """
  This class contains various functions that establishes connections to the server and db and executes SQL functions.
  """

  @classmethod
  def serv_conn(cls):
    """
    Establishes a connection to the server.
    :return
    connection: Returns the connection object.
    """
    connection = psycopg2.connect(
      host=config('DB_HOST'),
      port=config('DB_PORT'),
      database=None,
      user=config('DB_USER'),
      password=config('DB_PASSWORD'))
    cursor = connection.cursor()
    connection.autocommit = True
    cursor.execute('DROP DATABASE IF EXISTS projectdb')
    cursor.execute('CREATE DATABASE projectdb')
    return connection

  @classmethod
  def connect(cls):
    """
    Establishes a connection to the database.
    :return
    connection: Returns the connection object.
    """
    try:
      connection = psycopg2.connect(
        host=config('DB_HOST'),
        port=config('DB_PORT'),
        database=config('DB_NAME'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'))
      connection.autocommit = True
      return connection
    except psycopg2.Error as error:
      print("Error in connecting to postgreSQL server", error)
      return False

  @classmethod
  def setup(cls):
    """
    Execute the structure SQL scripts.
    :return
    None: Returns None.
    """
    cursor = cls.connect().cursor()
    with open('src/schemas/structure.sql') as sql_file:
      sql_query = sql_file.readlines()
      for line in sql_query:
          cursor.execute(line)

  @classmethod
  def seed(cls):
    """
    Execute the SQL script that inserts into pages table.
    :return
    None: Returns None
    """
    cls.setup()
    cursor = cls.connect().cursor()
    with open('src/schemas/seed.sql') as sql_file:
      sql_query = sql_file.readlines()
      for line in sql_query:
        cursor.execute(line)

  @classmethod
  def links(cls):
    """
    Executes the SQL scripts for links table.
    :return
    None: Returns None.
    """
    return Links(cls.connect())

  @classmethod
  def pages(cls):
    """
    Executes the SQL scripts for links table.
    :return
    None: Returns None.
    """
    return Pages(cls.connect())

