
import pandas as pd
import sqlite3
import csv
from TTS import TTS

class Database: 
    conn = sqlite3.connect("info.db")
    cursor = conn.cursor()
    row_list = [["event_id", "event_name", "event_date", "start_time", "end_time", "location", "description"],
                [1, "Ash Ketchum", 1970-1-1, 2340,2340,  "here", "N/A"],
                [2, "Gary Oak", 1970-1-1,2340,2340,  "here", "N/A" ],
                [3, "Brock Lesner", 1970-1-1, 2340,2340, "here", "N/A"]]

    with open('database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
    file.close()


    data = pd.read_csv ("database.csv")   
    df = pd.DataFrame(data) 


    # Connect to SQL Server (Microsoft Azure Support)
    # conn = pyodbc.connect('Driver={SQL Server};'
    #                       'Server=info;'
    #                       'Database=test_database;'
    #                       'Trusted_Connection=yes;')
    # cursor = conn.cursor()



    # Create Table
    cursor.execute("DROP TABLE IF EXISTS EVENTS")
    cursor.execute('''
            CREATE TABLE EVENTS (
    event_id INT PRIMARY KEY,
    event_name VARCHAR(255),
    event_date DATE,
    start_time INT,
    end_time INT,
    location VARCHAR(255),
    description TEXT)
    ''');


    # cursor.execute("DROP TABLE MASTER") # NOT IN USE
    # cursor.execute('''
    #         CREATE TABLE MASTER (
    #         "date"	TEXT,
	#         "completion" INTEGER
    #         )
    # ''');

    
    # cursor.execute("DROP TABLE IF EXISTS TASKS") # IN USE DO NOT DROP PLZ
#     cursor.execute('''
#        CREATE TABLE "TASKS" (
#     "task_id"    INTEGER NOT NULL,
#     "task_name"  TEXT,
#     "task_date"  TEXT,
#     "completion" INTEGER,
#     PRIMARY KEY("task_id")
#        );
# ''')
                   


    # cInsert DataFrame to Table
    for row in df.itertuples():
        cursor.execute('''
        INSERT INTO EVENTS (event_id, event_name, event_date, start_time, end_time, location, description)
        VALUES (?,?,?,?,?,?,?)
        ''',
                    (row.event_id, 
                    row.event_name,
                    row.event_date,
                    row.start_time, 
                    row.end_time, 
                    row.location, 
                    row.description
                    ))
        

    

    # conn = sqlite3.connect('info.db')
    def event_adder_conn(event_name, event_date, start_time, end_time, location, description):
        c = Database.conn.cursor()
        c.execute("INSERT INTO events (event_name, event_date, start_time, end_time, location, description) VALUES (?, ?, ?, ?, ?, ?)", (event_name, event_date, start_time, end_time, location, description))
        Database.conn.commit()

        # event_name = input("Enter the event name: ")
        # event_date = input("Enter the event date (YYYY-MM-DD): ")
        # start_time = input("Enter the start time (HH:MM:SS): ")
        # end_time = input("Enter the end time (HH:MM:SS): ")
        # location = input("Enter the location: ")
        # description = input("Enter a description: ")
    

    def task_adder_conn(task_name, task_date):
        c = Database.conn.cursor()
        c.execute("INSERT INTO TASKS (task_name, task_date, completion) VALUES (?, ?, ?)", (task_name, task_date, 0))
        Database.conn.commit()
        

    def task_puller(task_date): #obj: print tasks for the day
        Database.cursor.execute("SELECT * FROM TASKS WHERE task_date = ?", (task_date,))
        temp = Database.cursor.fetchall()
        Database.conn.commit()
        return temp

        
    def task_completion(completion_status):
        c = Database.conn.cursor()
        c.execute("INSERT INTO TASKS (,,,completion_status)")
        Database.conn.commit()
        

    # cursor.execute("SELECT* FROM TASKS") #general print
    # result = cursor.fetchall()
    # for row in result:
    #     print(row)
    #     print("\n")
    # conn.commit()
    


    # conn.close()  




    # print(df)
    # print("Hello World")

