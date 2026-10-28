# Full Year Calendar Generator
import calendar
year=int(input("Enter Year: "))
print("\n",calendar.calendar(year))

#Specific Month Calendar Viewer
import calendar
year=int(input("Enter Year: "))
month=int(input("Enter Month: "))
print("\n",calendar.month(year,month))

#Day Finder from Specific Date 
import datetime
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
day = int(input("Enter day: "))
date_obj = datetime.date(year, month, day)
print("\nDay:", date_obj.strftime("%A"))
