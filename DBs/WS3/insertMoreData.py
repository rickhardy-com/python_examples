from sqlite3 import connect

# data
DATA = (
    (0, 'Hello!'),
    (1, 'Computing'),
    (2, 'Is'),
    (3, 'The'),
    (4, 'Best'),
    (5, 'Subject'),
    (6, 'A*'),
)

# create an instance of the connect class
conn = connect('pythonex1.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS my_data (
                                     id integer,
                                     name text
                                   )'''
          )

# fill tables with data
for data_row in DATA:
    c.execute('INSERT into my_data VALUES (?,?)', data_row)

# commit and close
c.close()
conn.commit()
conn.close()
