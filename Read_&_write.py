import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('finance.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS payments(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def data_entry():
    c.execute("INSERT INTO payments VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO payments (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()
    time.sleep(1)

def read_from_db():
    c.execute('SELECT * FROM payments')
    # if you want a single row then cur.fetchone()
    data = c.fetchall()
    print(data)
    # we do not want the whole data we want to iterate in the data and for that we use for loop
    for row in data:
        print(row)

##    c.execute('SELECT * FROM payments WHERE value = 3')
##    data = c.fetchall()
##    print(data)
##    for row in data:
##        print(row)
##
##    c.execute('SELECT * FROM payments WHERE unix > 1452554972')
##    data = c.fetchall()
##    print(data)
##    for row in data:
##        print(row)
##
##    c.execute('SELECT value, datestamp FROM payments WHERE unix > 1452554972')
##    data = c.fetchall()
##    print(data)
##    for row in data:
##        print(row[0])
    
read_from_db()
c.close
conn.close()


