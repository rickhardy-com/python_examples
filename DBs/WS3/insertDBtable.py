from sqlite3 import connect

# Open a connection, if the database does not exist in the working directory this command will create it
conn = connect("pythonex1.db")

# create a cursor, this is a class with methods for database operations
cursor = conn.cursor()

# the cursors execute method runs the sql that it is passed to it and creates a tuple of tuples 
# the inner tuple is the returned row

cursor.execute("CREATE TABLE IF NOT EXISTS member (username TEXT, password TEXT)")  

cursor.execute("INSERT INTO MEMBER (username, password) VALUES('admin', 'admin')")
 
# you don't need to commit ddl statements like create and drop

conn.commit()

cursor.close()
conn.close()

