"""
Congratulations!
You are now in charge of the code that calculates business days.

The business team has requested that sofas can only be delivered 3 business days after they were sold.
A business day is any day of the week except Sundays and holidays.
You have been provided a list of company observed holidays.

Write code that takes the date the sofa was sold, calculate the delivery date, and return it.
Write tests to prove your code.
"""
from datetime import datetime, timedelta

holidays = [
    "2023-01-01",
    "2023-01-16",
    "2023-02-02",
    "2023-02-04",
    "2023-02-06",
    "2023-02-20",
    "2023-05-29",
    "2023-06-19",
    "2023-07-04",
    "2023-09-04",
    "2023-10-09",
    "2023-11-11",
    "2023-11-23",
    "2023-12-25",
]



def is_sunday(todays_date: datetime) -> bool:
    if todays_date.weekday() == 6:
        return True
    else:
        return False


def is_holiday(todays_date: datetime) -> bool:
    year = todays_date.year
    month = todays_date.month
    day = todays_date.day
    
    date = str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
    if date in holidays:
        return True
    else:
        return False       


def calculate_delivery_date(purchase_date: datetime) -> datetime:
    delivery_date = 0
    while delivery_date < 3:
        if is_holiday(purchase_date) and is_sunday(purchase_date):
            purchase_date = purchase_date + timedelta(days = 1)
            continue
        elif is_holiday(purchase_date):
            purchase_date = purchase_date + timedelta(days = 1)
            continue
        elif is_sunday(purchase_date):
            purchase_date = purchase_date + timedelta(days = 1)
            continue
            
        delivery_date += 1
        purchase_date = purchase_date + timedelta(days = 1)
    return purchase_date
 
purchase_date = datetime(2023, 1, 1)    
calculate_delivery_date(purchase_date)
    