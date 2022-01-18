from django.urls import path
from . import views

urlpatterns = [
    # blank path to indicate default as home page
    # and render this class as a view using 'as_view()'

    # path converter if matched to return a string, if not a 404 message

    # capture url and pass to calendar view
    path('event_calendar', views.event_calendar, name='event_calendar'),
    path('<int:year>/<str:month>/', views.event_calendar, name='event_calendar'),
    # path('all_events', views.all_events, name='all_events'),
    path('all_projects', views.all_projects, name='all_projects'),
    # path('add_venue', views.add_venue, name='add_venue'),
    path('add_people', views.add_people, name='add_people'),
    # path('all_venues', views.all_venues, name='all_venues'),
    path('all_people', views.all_people, name='all_people'),
    # path('show_venue/<int:venue_id>/', views.show_venue, name='show_venue'),
    path('show_people/<int:people_id>/', views.show_people, name='show_people'),
    # path('update_venue/<int:venue_id>/', views.update_venue, name='update_venue'),
    path('update_people/<int:people_id>/', views.update_people, name='update_people'),
    # path('add_event', views.add_event, name='add_event'),
    path('add_project', views.add_project, name='add_project'),

    ]
