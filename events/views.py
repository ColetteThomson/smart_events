from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

# function: dynamic title showing current month
# if year,month not passed to 'calendar' then will default to current month
def calendar(request, year=date.today().year, month=date.today().month):
    # convert year and month to integers
    year = int(year)
    month = int(month)
    # if year is less than 2000 or greater than 2099, set year to this year
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "Smart Events Calendar - %s %s" % (month_name, year)
    # retrieve HTML formatted calendar
    cal = HTMLCalendar().formatmonth(year, month)
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    