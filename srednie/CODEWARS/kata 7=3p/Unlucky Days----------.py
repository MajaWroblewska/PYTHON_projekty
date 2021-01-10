from datetime import date

def unlucky_days(year):
    return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))

unlucky_days()
################################################################################
from calendar import weekday

def unlucky_days(year):
    return sum(1 for i in xrange(1, 13) if weekday(year, i, 13) == 4)
#############################################################################
from datetime import datetime

def unlucky_days(year):
   return sum(datetime(year, month, 13).weekday() == 4 for month in range(1,13))

#############################################################################
from datetime import date
def unlucky_days(year):
    counter = 0
    for months in range(1,13):
        if date(year, months, 13).weekday()==4:
            counter +=1
    return counter

#############################################################################
def unlucky_days(year):
    import calendar
    fridays = 0
    for i in range(1,13):
        if calendar.weekday(year,i,13) == 4:
            fridays += 1
    return fridays
#############################################################################
