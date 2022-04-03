import sqlite3
import csv


conn = sqlite3.connect('ocr.db')


# create table



c = conn.cursor()
c.execute("DROP TABLE spec")

c.execute('''CREATE TABLE spec (
                                     level integer, 
                                     component_id text,
                                     component_text1 text,
                                     component_text2 text,
                                     parent_id text
                                   )'''
          )

with open('ocr2.csv') as f:
    
    csv_reader = csv.reader(f, delimiter=',')
    for i in csv_reader:
        print (i)
        
        c.execute('INSERT into spec VALUES (?,?,?,?,?)', i)
        #conn.commit()
        
c.close()
conn.commit()
conn.close()

#recursive to retrieve hierarchy

'''
WITH RECURSIVE componentx (component_id, component_text1, parent_id, sort, format1, format2) 
AS
(
select spec.component_id, spec.component_text1, spec.parent_id, component_id, level, ''
from spec 
WHERE spec.level = 1 -- and component_id = 1
UNION ALL
select e.component_id, e.component_text1, e.parent_id, 
       sort || ' ' || e.component_id,
       "-" || level || ' '  || e.component_id, 
	   ' '  || e.component_id
	   
from spec as e
inner join componentx o
         on o.component_id = e.parent_id


)
select component_id, component_text1, sort, format1, format2
 from componentx
order by sort
'''