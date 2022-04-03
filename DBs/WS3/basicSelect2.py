


#sqlite library
import sqlite3

employees_list = []

search_name = input ('Pattern to search for: ')

# open a connection 
conn = sqlite3.connect('chinook.db')

#Declare a cursor this is an recursive object that outputs a tuple for each row returned by the query

cur = conn.cursor()

for row in cur.execute ('SELECT  firstname, LastName FROM customers WHERE lastname LIKE "' + search_name +'"'):

    employees_list.append (row[0])


#Close the cursor and the connection

cur.close()
conn.close()

print (employees_list)
