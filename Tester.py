from dbconnect import Database as db 
import datetime as dt
from TTS import TTS

# db.task_adder_conn("Event 223","2023-05-23")
# print(db.task_puller2("2023-05-14","test event meeting",2)) 



# upcoming Sat and Sun. 

#upcoming Mon-Fri 
today = dt.date.today()
days_to_monday = (0 - today.weekday()) % 7
days_to_friday = (4 - today.weekday()) % 7

next_monday = today + dt.timedelta(days=days_to_monday)
next_friday = today + dt.timedelta(days=days_to_friday)

dates_of_week = []
names_for_dates = []
for i in range(5):
    date = today + dt.timedelta(days=i+days_to_monday)
    dates_of_week.append(date.strftime("%Y-%m-%d"))
    names_for_dates.append("PLACEHOLDER" + str(i))


# db.task_adder_conn(names_for_dates,dates_of_week)
# db.task_deleter(db.task_puller3(dates_of_week,None,1),None, 1)

# print(dates_of_week)

# #tomorrow 
# today = dt.date.today()
# tomorrow = today + dt.timedelta(days=1)
# tomorrow_date = [tomorrow.strftime("%Y-%m-%d")]

# print(tomorrow_date)

# #today
# today = dt.date.today()
# tomorrow = today + dt.timedelta(days=1)

# tomorrow_date = [tomorrow.strftime("%Y-%m-%d")]

# print(tomorrow_date)



