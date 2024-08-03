import sqlite3

connection=sqlite3.connect("students.db")

cursor=connection.cursor()
  

table_info="""CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25), MARKS INT);"""
cursor.execute(table_info) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',80)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',99)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C',55)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C',30)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('deepa', 'Data Science', 'C',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('diya', 'Devops', 'C',80)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('priya', 'Devops', 'C',70)''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()
