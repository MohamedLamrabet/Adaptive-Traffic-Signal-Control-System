import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="traffic")

# creating the cursor object
cur = myconn.cursor()

try:
    # Creating a table with name Employee having four columns i.e., name, id, salary, and department id
    dbs = cur.execute(
        "create table statistics(id int(20) not null primary key, lane int(20) not null, no_vehicles int(20) not null, time int(20) not null)")
except:
    myconn.rollback()

myconn.close()