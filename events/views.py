from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event

def event_calendar(request, todays_date=date.today()):
    name = "Marty"
    year = todays_date.year
    month = todays_date.strftime('%B')
    month_number = todays_date.month
    # convert month from characters to number
    # month_no = str(calendar.month_name).calendar(month)
    # month_no = int(month_no)

    # create calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    return render(request,
                'event_calendar.html', {
                "name": name,
                "year": year,
                "month": month,
                "month_no": month_number,
                "cal": cal,
                })

# def calendar(request, year=date.today().year, month=date.today().month):
    # convert year and month to integers
    # year = int(year)
    # month = int(month)
    # if year < 1900 or year > 2099:
    #     year = date.today().year
    # month_name = calendar.month_name[month]
    # title = "Smart Events Calendar - %s %s" % (month_name, year)
    # # retrieve HTML formatted calendar
    # cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    

# function: dynamic title showing current month
# if year,month not passed to 'calendar' then will default to current month
# def calendar(request, year=date.today().year, month=date.today().month):
    # convert year and month to integers
    # year = int(year)
    # month = int(month)
    # if year is less than 2000 or greater than 2099, set year to this year
    # if year < 2000 or year > 2099: year = date.today().year
    # month_name = calendar.month_name[month]
    # title = "Smart Events Calendar - %s %s" % (month_name, year)
    # retrieve HTML formatted calendar
    # cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))

    # t = date.today()
    # month = date.strftime(t, '%b')
    # year = t.year

    # return render(
     #    request,
       #  "calendar.html",
        # {
          #  'title': title,
           # 'cal': cal
        #}
    #)
    

#def all_events(request):
   # event_list = Event.objects.all()
    #return render(
       # request,
      #  "events/event_list.html",
      #  {'event_list': event_list}
  #  )
