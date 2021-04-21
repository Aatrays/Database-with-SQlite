# https://sqlite.org/datatype3.html
# SQLite truly shines because it is extremely lightweight. Setting up an SQLite database is nearly instant,
# there is no server to set up, no users to define, and no permissions to concern yourself with. For this reason,
# it is often used as a developmental and protyping database, but it can and is used in production.

# First, we need to establish a connection and cursor. This is for both SQLite and MySQL:

import sqlite3

conn = sqlite3.connect('finance.db')

# Define the cursor that will help us to do things like select, delete or add.
cur = conn.cursor()

# Creating Table if there is no existence of table
# it has 4 rows unix, datestamp, keyword asnd value.
def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS payments(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    # inserting values to the table payment the values are tuple
    cur.execute("INSERT INTO payments VALUES(1245789,'2021-04-21 13:53:39','Python',60000)")

    # to save the changes 
    conn.commit()
    cur.close()
    conn.close()

create_table()
data_entry()
