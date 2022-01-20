from datetime import datetime
from datetime import date
import calendar
from calendar import HTMLCalendar

from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Project, People
from .forms import PeopleForm, ProjectForm

# Pagination
from django.core.paginator import Paginator


# --------------------------------------------------- Functions for 'PROJECT'

# DELETE a project
def delete_project(request, project_id):
    # get primary key project_id from Project
    project = Project.objects.get(id=project_id)
    # delete the project
    project.delete()
    # redirect back to 'all_projects' page
    return redirect('all_projects')


# UPDATE a project
def update_project(request, project_id):
    # get primary key project_id from Project
    project = Project.objects.get(id=project_id)
    # if form completed and submitted then Post, or
    # if not then display empty ProjectForm
    form = ProjectForm(request.POST or None, instance=project)
    # if project form is valid (required fields completed)
    if form.is_valid():
        # save and return to all_projects (url)
        form.save()
        return redirect('all_projects')
        
    # update individual projects
    return render(request,
                  'update_project.html', {
                                     "project": project,
                                     "form": form,
                                    })

# CREATE (add) a new project
def add_project(request):
    # obtain all data posted from form
    project_form = ProjectForm(data=request.POST)

    # if project form is valid (required fields completed)
    if project_form.is_valid():
        # save to database
        new_project = project_form.save(commit=False)
        # then save the new project
        new_project.save()

        return render(request,
                      'add_project.html', {
                                    'project_form': project_form,
                                    'submitted': True,
                                    })
    else:
        project_form = ProjectForm()
        # check if user submitted form
        if 'submitted' in request.GET:
            submitted = True

        return render(request,
                      'add_project.html', {
                                       'project_form': project_form,
                                        })


# LIST all projects
def all_projects(request):
    # call all Project objects from models.py
    project_list = Project.objects.all().order_by('project_name', 'project_manager')
    # list all projects on one page
    return render(request,
                  'all_projects.html', {
                                     "project_list": project_list,
                                    })

# --------------------------------------------------- Functions for 'PEOPLE'

# SEARCH for people
def search_people(request):
    # if user clicks 'search' button
    if request.method == "POST":
        # variable to contain entered search request
        searched = request.POST['searched']
        # search for person_name that contains search request
        persons = People.objects.filter(person_name__contains=searched)
        # return search result
        return render(request,
                      'search_people.html', {
                                             'searched': searched,
                                             'persons': persons,
                                            })
    else:
        # return search result
        return render(request,
                      'search_people.html', 
                      {})


# DELETE a person from 'people'
def delete_people(request, people_id):
    # get primary key people_id from People
    people = People.objects.get(id=people_id)
    # delete the person
    people.delete()
    # redirect back to 'all_people' page
    return redirect('all_people')


# UPDATE people
def update_people(request, people_id):
    # get primary key people_id from People
    people = People.objects.get(id=people_id)
    # if updating then pre-populate existing info (instance)
    # if not then display empty PeopleForm
    form = PeopleForm(request.POST or None, instance=people)
    # if people form is valid (required fields completed)
    if form.is_valid():
        # save and send to all_people page 
        form.save()
        return redirect('all_people')
        
    # update individual people
    return render(request,
                  'update_people.html', {
                                     "people": people,
                                     "form": form,
                                    })


# SHOW individual people
def show_people(request, people_id):
    # get primary key people_id from People
    person = People.objects.get(id=people_id)
    # show individual people
    return render(request,
                  'show_people.html', {
                                     "person": person,
                                    })


# LIST all people
def all_people(request):
    # call all People objects from models.py
    ###people = People.objects.all().order_by('person_name')
    people = People.objects.all()
    # set up pagination, show 2 people per page
    p = Paginator(People.objects.all(), 2)
    # return the page
    page = request.GET.get('page')
    people_list = p.get_page(page)

    # list all people 
    return render(request,
                  'all_people.html', {
                                     "people": people,
                                     "people_list": people_list,
                                    })


# CREATE (add) new people
def add_people(request):
    # obtain all data posted from form
    people_form = PeopleForm(data=request.POST)

    # if people form is valid (required fields completed)
    if people_form.is_valid():
        # save to database
        new_people = people_form.save(commit=False)
        # then save the new people
        new_people.save()

        return render(request,
                      'add_people.html', {
                                    'people_form': people_form,
                                    'submitted': True,
                                    })
    else:
        people_form = PeopleForm()
        # check if user submitted form
        if 'submitted' in request.GET:
            submitted = True

        return render(request,
                      'add_people.html', {
                                       'people_form': people_form,
                                        })


# project calendar
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
