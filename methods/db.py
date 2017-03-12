import mysql.connector
from mysql.connector import errorcode

try:
  config = {
    'user': 'root',
    'password': 'Aa8411089ajgedbaa',
    'host': '127.0.0.1',
    'database': 'db1',
    }

  cnx = mysql.connector.connect(**config)
  cnx.set_autocommit( True )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)


