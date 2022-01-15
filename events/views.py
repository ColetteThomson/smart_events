from datetime import datetime
from datetime import date
import calendar
from calendar import HTMLCalendar

from django.shortcuts import render
from django.views import generic, View
from .models import Event
from .forms import VenueForm


def add_venue(request):
    # obtain all data posted from form
    venue_form = VenueForm(data=request.POST)

    # if venue form is valid (required fields completed)
    if venue_form.is_valid():
        # save to database
        new_venue = venue_form.save(commit=False)
        # then save the new venue
        new_venue.save()

        return render(request,
                      'add_venue.html', {
                                    'venue_form': venue_form,
                                    'submitted': True,
                                    })

    else:
        venue_form = VenueForm()
        # check if user submitted form
        if 'submitted' in request.GET:
            submitted = True

        return render(request,
                      'add_venue.html', {
                                       'venue_form': venue_form,
                                        })


def all_events(request):
    event_list = Event.objects.all()

    return render(request,
                  'all_events.html', {
                                     "event_list": event_list,
                                    })


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
