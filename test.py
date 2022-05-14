import sqlite3


# this is used to connect to the data base and need to insert the name of the data base inside
connection = sqlite3.connect('data.db')

# this is used to initalize the cursor and insert data and tell us the data in the data base and it performs operations
cursor = connection.cursor()  

#this creates a table and we mention quires as strings
#the fields inside the table are mentioned inside the parentasis 
create_table = "CREATE TABLE users (id int,username text,password text)"

#this is the command used to exexute quires
cursor.execute(create_table)

user = (1,'varun','testing#1')

#this is to build a quirey 
insert_quirey = "INSERT INTO users Values (?,?,?)"


cursor.execute(insert_quirey,user)

users = [
    (2,'vedu','temp'),
    (3,'vamshi','testing')
    ]

cursor.executemany(insert_quirey,users)

select_quirey="SELECT * from users"

for row in cursor.execute(select_quirey):
    print(row)
#this is used to commit the changes
connection.commit()

#this is used to close the connection
connection.close()