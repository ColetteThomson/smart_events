from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from datetime import date
from datetime import datetime
import calendar
from calendar import HTMLCalendar
from .models import Event

def event_calendar(request, todays_date=date.today()):
    name = "Marty"
    year = todays_date.year
    month = todays_date.strftime('%B')
    month_number = todays_date.month
    
    # create calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)
    
    # get current year
    now = datetime.now()
    current_year = now.year

    return render(request,
                  'event_calendar.html', {
                                          "name": name,
                                          "year": year,
                                          "month": month,
                                          "month_no": month_number,
                                          "cal": cal,
                                          "current_year": current_year,
                                        })


# def all_events(request):
#     event_list = Event.objects.all()
#     return render(request,
#         'events/event_list.html',
#         {"event_list": event_list}
#     )
