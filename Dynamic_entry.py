import sqlite3
import time
import datetime
import random # to import random values

conn = slqite3.commect('finance.db')

cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS payments(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    cur.execute("INSERT INTO payments VALUES(1245789,'2021-04-21 13:53:39','Python',60000)")
 
    conn.commit()
    cur.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    # (unix, datestamp, keyword, value) - the order can be change but we can not enter only three coloumns
    # ? is for sqlite and %s for mysql
    cur.execute("INSERT INTO payments (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)",
                (unix, date, keyword, value))
    con.commit()
    # we do not have to close the connection everytime we enter in tables

create_table()
#data_entry()

for i range(10):
    dynamic_data_entry()
    time.sleep(1)

cur.close()
conn.close()

