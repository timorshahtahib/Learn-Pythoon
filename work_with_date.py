from datetime import date
from datetime import datetime

from datetime import timedelta

today=date.today()

print("today time is {}".format(today))

print("date is ",today.day,today.month,today.year)

now=datetime.now()#comple today date
print(now)

print("year :" ,now.strftime("%Y"))

print(now.strftime("%A,%d,%b,%Y"))#Wednesday,09,Mar,2022
print(now.strftime("%A,%d,%b,%Y  - %I:%M:%S  %p"))#Wednesday,09,Mar,2022  - 04:45:04  PM

oneyear=datetime.now()+timedelta(days=365,hours=2)#2023-03-09 19:46:03.139444

print("one year later" ,oneyear)