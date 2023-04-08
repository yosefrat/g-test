# That classic shit

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="secret-g",
  port=3307,
  database="test_houses"
)

# Cursor
cur = mydb.cursor()

# Retrieve
result = cur.callproc('how_many_houses',['Jamille',0])

the_number_of_houses_jamille_has = result[1]

print("Jamille has {0} houses".format(the_number_of_houses_jamille_has))