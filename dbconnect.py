
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


    def task_adder_conn(task_names, task_dates):
        c = Database.conn.cursor()
        num = 0 
        for i  in task_names: 
            task_name = i
            task_date = task_dates[num]
            num+=1
            c.execute("INSERT INTO TASKS (task_name, task_date, completion) VALUES (?, ?, ?)", (task_name, task_date, 0))
        Database.conn.commit()
        

  
            

    def task_puller2(task_date,task_name,field): #obj: print tasks for the day (in progress)
        result  = []
        if field == 1: 
            Database.cursor.execute("SELECT * FROM TASKS WHERE task_date = ?", (task_date,))
            temp = Database.cursor.fetchall()
            result.extend([row[field] for row in temp])
        if field == 2:
            Database.cursor.execute("SELECT * FROM TASKS WHERE task_name = ?", (task_name,))
            temp = Database.cursor.fetchall()
            result.extend([row[field] for row in temp])
        for row in temp: 
            print(row[field])
            print("\n")
        Database.conn.commit()
        return result
    

    def task_puller3(task_dates, task_name, field):
        result = []
        if field == 1: 
            for task_date in task_dates:
                Database.cursor.execute("SELECT * FROM TASKS WHERE task_date = ?", (task_date,))
                temp = Database.cursor.fetchall()
                result.extend([row[field] for row in temp])
                for row in temp: 
                    print(row[field])
                    print("\n")
        if field == 2:
            Database.cursor.execute("SELECT * FROM TASKS WHERE task_name = ?", (task_name,))
            temp = Database.cursor.fetchall()
            result.extend([row[field] for row in temp])
            for row in temp: 
                print(row[field])
                print("\n")
        Database.conn.commit()
        return result

    
    
    
    def task_set_name(old_task_name,new_task_name):
        c = Database.conn.cursor()
        c.execute('UPDATE TASKS SET task_name = ? WHERE task_name= ?', (new_task_name, old_task_name))
        Database.conn.commit()

    def task_set_date(task_name,new_task_date):
        c = Database.conn.cursor()
        c.execute('UPDATE TASKS SET task_date = ? WHERE task_name= ?', (new_task_date, task_name))
        Database.conn.commit()
        
    def task_set_completion(completion_status,task_name): #completion status should be a one or a zero 
        c = Database.conn.cursor()
        c.execute('UPDATE TASKS SET completion = ? WHERE task_name= ?' , (completion_status,task_name))
        Database.conn.commit()

    def task_deleter(name_of_tasks, ID_of_tasks, field ): #field 1. call using name #field 2. call using ID
        tasks_deleted = Database.task_puller3(name_of_tasks,None,1)
        c = Database.conn.cursor()
        if field == 1: 
            for i in name_of_tasks: 
                name_of_task = i
                c.execute('DELETE FROM TASKS WHERE task_name = ? ',   (name_of_task,))
        if field == 2: 
            for i in ID_of_tasks:
                id_of_task = i
                c.execute('DELETE FROM TASKS WHERE task_id = ? ',(id_of_task,))
        Database.conn.commit()
        return tasks_deleted
    


        



     
        

    # cursor.execute("SELECT* FROM TASKS") #general print
    # result = cursor.fetchall()
    # for row in result:
    #     print(row)
    #     print("\n")
    # conn.commit()
    


    # conn.close()  




    # print(df)
    # print("Hello World")

