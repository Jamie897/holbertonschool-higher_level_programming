import MySQLdb
import sys

# Get command-line arguments
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)
cursor = db.cursor()

# Execute the SQL query
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch and display the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the database connection
db.close()
