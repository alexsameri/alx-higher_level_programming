#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) == 4:
        # Get the arguments
        mysql_user = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]

        # Connect to the database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=db_name
        )

        # Get a cursor to execute queries
        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

        # Close the database connection
        db.close()

    else:
        # Print the usage instructions
        print("Usage: {} mysql_user mysql_password db_name".format(sys.argv[0]))
