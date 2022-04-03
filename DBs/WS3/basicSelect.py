
# sqlite library
from sqlite3 import connect

# open a connection 
conn = connect('chinook.db')

# Declare a cursor this is an recursive object that outputs a tuple for each row returned by the query
cur = conn.cursor()

for invoice_row in cur.execute ('SELECT * FROM invoices WHERE total >20'):
    print (invoice_row)
    print (type(invoice_row))

# Close the cursor and the connection in order
cur.close()
conn.close()

