from dbconnect import Database as db 

# db.task_adder_conn("test event", "2003-03-23")

print("\n" + str(db.task_puller("2003-03-23")) + "\n")
array = db.task_puller("2003-03-23") #function  obj not scriptable 
print(array[0][2])





