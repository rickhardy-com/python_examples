

import sqlite3

# data
VARIABLES = (
    (1, 'foo', 'ModuleExt', 'double', 'Description of foo'),
    (2, 'bar', 'ModuleExt', 'double', 'Description of bar'),
    (3, 'knark', 'Module1', 'int', 'Description of knark'),
    (4, 'wert', 'Module1', 'double', 'Description of wert'),
    (5, 'jib', 'Module1', 'double', 'Description of jib'),
    (6, 'laz', 'Module2', 'double', 'Description of laz'),
    (7, 'kew', 'Module2', 'double', 'Description of kew'),
)
FUNCTIONS = (
    (1, 'ExtSource'),
    (2, 'DoThis'),
    (3, 'CalcThis'),
    (4, 'CalcThat'),
    (5, 'ModifyStuff'),
    (6, 'ExtSink'),
)
VAR_FUNC = (
    (1, 1, 'output'),
    (1, 2, 'input'),
    (1, 4, 'input'),
    (2, 1, 'output'),
    (2, 2, 'input'),
    (2, 3, 'input'),
    (3, 2, 'input-output'),
    (3, 3, 'input'),
    (4, 2, 'output'),
    (4, 4, 'input'),
    (4, 5, 'input'),
    (5, 3, 'output'),
    (5, 5, 'input'),
    (6, 3, 'output'),
    (6, 5, 'output'),
    (6, 6, 'input'),
    (7, 4, 'output'),
    (7, 5, 'output'),
    (7, 6, 'input'),
)

# get connection and cursor objects
conn = sqlite3.connect('iodatabase.db')
c = conn.cursor()

# create tables
c.execute('''create table variable (
    id integer,
    name text,
    module text,
    type text,
    desc text
)''')
c.execute('''create table function (
    id integer,
    name text
)''')
c.execute('''create table var_func (
    variable_id integer,
    function_id integer,
    type text
)''')

# fill tables with data
for row in VARIABLES:
    c.execute('insert into variable values (?,?,?,?,?)', row)
for row in FUNCTIONS:
    c.execute('insert into function values (?,?)', row)
for row in VAR_FUNC:
    c.execute('insert into var_func values (?,?,?)', row)

#use the join to make links between the different relational tables for the query - referential integrity
c.execute(''.join([
            'SELECT variable.name, variable.module, variable.type, variable.desc ',
            'FROM variable, var_func, function ',
            'WHERE variable.id=var_func.variable_id ', 
            'AND function.id=var_func.function_id ',
            'AND function.name="CalcThis" ',
            'AND var_func.type="output" ',
            ]))
FORMAT = '%-6s%-10s%-8s%-20s'
print (FORMAT % ('name', 'module', 'type', 'desc'))
print ('-' * 44)
for row in c:
    print (FORMAT % row)

#use the join to make links between the different relational tables for the query - referential integrity
c.execute(''.join([
            'SELECT function.name ',
            'FROM variable, var_func, function ',
            'WHERE variable.id=var_func.variable_id ', 
            'AND function.id=var_func.function_id ',
            'AND variable.name="wert" ',
            'AND var_func.type="input" ',
            ]))
print ('name')
print ('------------')
for row in c:
    print ('%s' % row)

c.close()
conn.commit()
conn.close()
