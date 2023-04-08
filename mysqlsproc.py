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

# Set who
owner = 'Jamille'

# Retrieve the result of the cursor
scalar = cur.callproc('how_many_houses',[owner,0])

# Set a var on the resultset
the_number_of_houses_jamille_has = scalar[1]

# Print the result in a string
print("If we look for {0}'s homes, he has {1} houses".format(owner,the_number_of_houses_jamille_has))
print("=============")


# Call the proc that returns rows instead of a scalar, dictating you want back 5 rows at most
# Note the empty parameter for the OUT since this is a table-valued result, not a scalar. 
# That's intentional, and poorly documented in the MySQL Connector API.
cur.callproc('all_house_count',[5,])

# Instantiate the result set, note this instantiates a list object but you're fetching only once
rows = cur.stored_results()

# Create a new list for your rows. The semantics of `row.fetchall()` doesn't really make any sense conceptually since you're only ever
# executing one procedure, but is apparently how the API is setup in this library.
for row in rows:
	all_house_owners = row.fetchall()

# Print the results
print("What if we want to know all owners?")
for owner in all_house_owners:
	print("{0} owns {1}".format(owner[0],owner[1]))

# Be a good citizen to your db and close your cursor
cur.close()