"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""


import sqlite3
from pandas import DataFrame



conn = sqlite3.connect ( 'db_University.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE student(
          
          Student_Name  TEXT,
          
          Student_Age INTEGER,
          Student_Roll_no TEXT,
          Student_Branch TEXT
          
          )""")


# STEP 2
c.execute("INSERT INTO student VALUES ('manas',20, '12', 'cse')")
c.execute("INSERT INTO student VALUES ('manas',22, '13', 'cse')")
c.execute("INSERT INTO student VALUES ('manas',21, '14', 'cs')")
c.execute("INSERT INTO student VALUES ('manas',19, '17', 'ee')")
c.execute("INSERT INTO student VALUES ('manas',20, '128', 'ce')")


# STEP 3
c.execute("SELECT * FROM student")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()


