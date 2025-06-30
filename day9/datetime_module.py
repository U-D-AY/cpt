from datetime import datetime, date, timedelta

# current time and date
now = datetime.now()
print(f"Current datetime: {now}")

# only date
print(f'Today date: {datetime.now()}')

#formatted datetime
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(f"formatted datetime : {formatted}")

# parsed datetime
date_str = "26-11-2004 1:15:26"
parsed = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print(parsed)

#timedelta
tomorrow = datetime.now()+timedelta(days=1)
print(f"Tomorrow: {tomorrow}")
yesterday = datetime.now()-timedelta(days=1)
print(f"Yesterday: {yesterday}")
ftime = now+timedelta(hours=5,minutes=50)
print(f"After 5:50 = {ftime}")