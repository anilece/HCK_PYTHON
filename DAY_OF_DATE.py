# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
date=input()
year=int(date[6:10])
day=int(date[3:5])
month=int(date[0:2])
DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
date = DayL[datetime.date(year,month,day).weekday()] + 'day'
#Set day, month, year to your value
#Now, date is set as an actual day, not a number from 0 to 6.

print(date.upper())
