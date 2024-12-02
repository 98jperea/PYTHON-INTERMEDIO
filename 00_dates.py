
from datetime import datetime

now = datetime.now()

#now = datetime.fromordinal(123456)

print(now.hour,now.minute,now.second,now.day,now.month)

timestamp = now.timestamp()

print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

from datetime import time

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.min)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date (24,12,25)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,current_date.month,current_date.day)

print(current_date.month)

diff = year_2023 - now
print(diff)

# (WRONG) from datetime import time
diff = year_2023.date() - current_date
print(diff)
print(year_2023.time())

from datetime import timedelta

start_timedelta = timedelta(200,100,100,weeks = 10)
end_timedelta = timedelta(300,100,100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

"""time_delta = timedelta()"""