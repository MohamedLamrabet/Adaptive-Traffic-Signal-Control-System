import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="traffic")

# creating the cursor object
cur = myconn.cursor()

no_of_vehicles = []

baseTimer = 120  # baseTimer = int(input("Enter the base timer value"))
timeLimits = [5, 30]  # timeLimits = list(map(int,input("Enter the time limits ").split()))
no_of_lanes = 2

try:
    # Reading the table data

    cur.execute("SELECT count FROM tracking WHERE id IN (SELECT MAX(id) FROM tracking GROUP BY lane);")

    # cur.execute("SELECT count FROM tracking WHERE lane=1 ORDER BY ID DESC LIMIT 1")

    # fetching the rows from the cursor object
    result = cur.fetchall()

    # printing the result

    for x in result:
        print(x[0])
        no_of_vehicles.append(x[0])

    # print("Input no of vehicles : ", *no_of_vehicles)
    t = [(i / sum(no_of_vehicles)) * baseTimer if timeLimits[0] < (i / sum(no_of_vehicles)) * baseTimer < timeLimits[1]
    else min(timeLimits, key=lambda x: abs(x - (i / sum(no_of_vehicles)) * baseTimer)) for i in no_of_vehicles]

    for no in range(no_of_lanes):
        print(f"* lane {no+1} => No of vehicles: {no_of_vehicles[no]} => Time: {t[no]}s")

    print(f"* Total of vehicles: {sum(no_of_vehicles)} => Total time: {sum(t)}s")

    for no in range(no_of_lanes):
        sql = "insert into statistics(id, lane, no_vehicles, time) values (%s, %s, %s, %s)"
        val = (no+1, no+1, no_of_vehicles[no], t[no])
        cur.execute(sql, val)
        myconn.commit()

except:
    myconn.rollback()

myconn.close()
