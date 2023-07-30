  # def task_puller(task_dates): #obj: print tasks for the day (decomisioned)
    #     result  = []
    #     for i in task_dates:
    #         task_date =  i
    #         Database.cursor.execute("SELECT task_name FROM TASKS WHERE task_date = ?", (task_date,))
    #         temp = Database.cursor.fetchall()
    #         result.extend([row[0] for row in temp])
    #         for row in temp: 
    #             print(row[0])
    #             print("\n")
    #     Database.conn.commit()
    #     return result
    