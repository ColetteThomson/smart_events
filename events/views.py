# from datetime import datetime
# from datetime import date
from django.shortcuts import render, redirect, reverse
# from django.views import View
# generic
#from django.contrib.auth.decorators import login_required
# Pagination
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Project, PeopleAdministration, PeopleTechSupport
from .forms import AdminForm, ProjectForm, TechSupportForm


# --------------------------------------------------- Functions for 'PROJECT'

# SEARCH for projects
def search_projects(request):
    """ if user clicks 'search' button """
    if request.method == "POST":
        # variable to contain entered search request
        searched = request.POST['searched']
        # search for project_name that contains search request
        projects = Project.objects.filter(project_name__contains=searched)
        # return search result
        return render(request,
                      'search_projects.html', {
                                             'searched': searched,
                                             'projects': projects,
                                            })
    else:
        # return search result
        return render(request,
                      'search_projects.html',
                      {})


# DELETE a project
def delete_project(request, project_id):
    """ get primary key project_id from Project """
    project = Project.objects.get(id=project_id)
    # if user is project manager (prevent deletion through url)
    if request.user == project.project_manager:
        # then delete the project
        project.delete()
        # display success message to user
        messages.success(request, ("Project has been deleted"))
        # redirect back to 'all_projects' page
        return redirect('all_projects')
    else:
        # display error message to user
        messages.warning(request,
                         ("You are not authorised to delete this project"))
        # redirect back to 'all_projects' page
        return redirect('all_projects')


# UPDATE a project
def update_project(request, project_id):
    """ get primary key project_id from Project """
    project = Project.objects.get(id=project_id)
    # if form completed and submitted then Post, or
    # if not then display empty ProjectForm
    form = ProjectForm(request.POST or None, instance=project)
    # if project form is valid (required fields completed)
    if form.is_valid():
        # save and return to all_projects (url)
        form.save()
        # display success message to user
        messages.success(request, ("Project has been updated"))
        return redirect('all_projects')

    # update details of a project
    return render(request,
                  'update_project.html', {
                                     "project": project,
                                     "form": form,
                                    })


# CREATE (add) a new Project
def add_project(request):
    """ check if user is ProjMgr1 """
    if request.user.username != 'ProjMgr1':
        return redirect('/')

    # obtain all data posted from project form
    project_form = ProjectForm()
    # if user has submitted form
    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST)
        # if user has permission to add a project
        if request.user.has_perm("events.add_project"):
            # if project form is valid (required fields completed)

            if project_form.is_valid():
                # save to database
                new_project = project_form.save(commit=False)
                # pass in logged in user.id as 'owner'
                new_project.project_manager = User.objects.get(
                    id=request.user.id)
                # then save the new project
                new_project.save()
                # redirect authorised user back to 'all_projects' page
                return redirect(reverse('all_projects'))

            else:
                # display error message to user
                messages.warning(request,
                                 ("'Description' allows 1000 characters only"))
        else:
            # display error message to user
            messages.warning(request,
                             ("You are not authorised to add a project"))

    else:
        # return form for authorised user to complete
        return render(request,  'add_project.html',
                      {'project_form': project_form})


# LIST all projects
def all_projects(request):
    """ call all Project objects from models.py """
    project = Project.objects.all()
    # set up pagination, show 2 projects per page
    p = Paginator(Project.objects.all(), 6)
    # return the page
    page = request.GET.get('page')
    project_list = p.get_page(page)

    # list all projects on one page
    return render(request,
                  'all_projects.html', {
                                     "project": project,
                                     "project_list": project_list,
                                    })


# SHOW details of a project
def show_project(request, project_id):
    """ get unique key project_id from Project """
    project = Project.objects.get(id=project_id)
    # show individual people
    return render(request,
                  'show_project.html', {
                                     "project": project,
                                     })


# ------------------------------------------------ Functions for 'ADMIN PEOPLE'

# SEARCH for people
def search_admin_people(request):
    """ if user clicks 'search' button """
    if request.method == "POST":
        # variable to contain entered search request
        searched = request.POST['searched']
        # search for person_name that contains search request
        persons = PeopleAdministration.objects.filter(
            person_name__contains=searched)
        # return search result
        return render(request,
                      'search_admin_people.html', {
                                             'searched': searched,
                                             'persons': persons,
                                            })
    else:
        # return search result
        return render(request,
                      'search_admin_people.html',
                      {})


# DELETE a person from Admin People
def delete_admin_people(request, people_id):
    """ get primary key people_id from PeopleAdmin """
    people = PeopleAdministration.objects.get(id=people_id)
    # if user is owner (prevent deletion through url)
    if request.user == people.ad_owner:
        # then delete the person
        people.delete()
        # display success message to user
        messages.success(request, ("Person has been deleted"))
        # redirect back to 'all_admin_people' page
        return redirect('all_admin_people')
    else: 
        # display error message to user
        messages.warning(request,
                         ("You are not authorised to delete this person"))
        # redirect back to 'all_admin_people' page
        return redirect('all_admin_people')


# UPDATE Admin People
def update_admin_people(request, people_id):
    """ get primary key people_id from PeopleAdmin """
    people = PeopleAdministration.objects.get(id=people_id)
    # if updating then pre-populate existing info (instance)
    # if not then display empty AdminForm
    form = AdminForm(request.POST or None, instance=people)
    # if admin form is valid (required fields completed)
    if form.is_valid():
        # save and send to all_admin_people page 
        form.save()
        # display success message to user
        messages.success(request, ("Admin Person has been updated"))
        return redirect('all_admin_people')

    # update details of a person
    return render(request,
                  'update_admin_people.html', {
                                                "people": people,
                                                "form": form,
                                              })


# SHOW details of a person
def show_admin_person(request, people_id):
    """ get unique key people_id from PeopleAdmin """
    person = PeopleAdministration.objects.get(id=people_id)
    # show individual people
    return render(request,
                  'show_admin_person.html', {
                                             "person": person,
                                            })


# LIST all Admin People
def all_admin_people(request):
    """ call all PeopleAdmin objects from models.py """
    people = PeopleAdministration.objects.all()
    # set up pagination, show 2 people per page
    p = Paginator(PeopleAdministration.objects.all(), 6)
    # return the page
    page = request.GET.get('page')
    people_list = p.get_page(page)

    # list all admin people 
    return render(request,
                  'all_admin_people.html', {
                                     "people": people,
                                     "people_list": people_list,
                                    })


# CREATE (add) new Admin People
def add_admin_people(request):
    """ check if user is PeopleAdmin """
    if request.user.username != 'PeopleAdmin':
        return redirect('/')

    # obtain all data posted from admin form
    admin_form = AdminForm()
    # if user has submitted form
    if request.method == 'POST':
        admin_form = AdminForm(data=request.POST)
        # if user has permission to add a person
        if request.user.has_perm("events.add_peopleadministration"):
            # if admin form is valid (required fields completed)

            if admin_form.is_valid():
                # save to database
                new_people = admin_form.save(commit=False)
                # pass in logged in user.id as 'owner'
                new_people.ad_owner = User.objects.get(id=request.user.id)
                # then save the new person
                new_people.save()
                # redirect authorised user back to 'all_admin_people' page
                return redirect(reverse('all_admin_people'))

            else:
                # display error message to user
                messages.warning(request,
                                 ("'Experience' allows 400 characters only"))
        else:
            # display error message to user
            messages.warning(request,
                             ("You are not authorised to add a person"))

    else:
        # return form for authorised user to complete
        return render(request,  'add_admin_people.html',
                      {'admin_form': admin_form})

# ---------------------------------------- Functions for 'TECH SUPPORT PEOPLE'

# SEARCH for Tech Support people
def search_techsupport_people(request):
    """ if user clicks 'search' button """
    if request.method == "POST":
        # variable to contain entered search request
        searched = request.POST['searched']
        # search for person_name that contains search request
        persons = PeopleTechSupport.objects.filter(
            person_name_tech__contains=searched)
        # return search result
        return render(request,
                      'search_techsupport_people.html', {
                                             'searched': searched,
                                             'persons': persons,
                                            })
    else:
        # return search result
        return render(request,
                      'search_techsupport_people.html',
                      {})


# DELETE a person from Tech Support People
def delete_techsupport_people(request, people_id):
    """ get primary key people_id from PeopleTechSupport """
    people = PeopleTechSupport.objects.get(id=people_id)
    # if user is owner (prevent deletion through url)
    if request.user == people.ts_owner:
        # then delete the person
        people.delete()
        # display success message to user
        messages.success(request, ("Person has been deleted"))
        # redirect back to 'all_techsupport_people' page
        return redirect('all_techsupport_people')
    else:
        # display error message to user
        messages.warning(request,
                         ("You are not authorised to delete this person"))
        # redirect back to 'all_techsupport_people' page
        return redirect('all_techsupport_people')


# UPDATE Tech Support People
def update_techsupport_people(request, people_id):
    """ get primary key people_id from PeopleTechSupport """
    people = PeopleTechSupport.objects.get(id=people_id)
    # if updating then pre-populate existing info (instance)
    # if not then display empty TechSupportForm
    form = TechSupportForm(request.POST or None, instance=people)
    # if tech support form is valid (required fields completed)
    if form.is_valid():
        # save and send to all_techsupport_people page
        form.save()
        # display success message to user
        messages.success(request, ("Tech Support Person has been updated"))
        return redirect('all_techsupport_people')

    # update details of a tech support person
    return render(request,
                  'update_techsupport_people.html', {
                                     "people": people,
                                     "form": form,
                                    })


# SHOW details of an Tech Support person
def show_techsupport_person(request, people_id):
    """ get unique key people_id from PeopleTechSupport """
    person = PeopleTechSupport.objects.get(id=people_id)
    # show individual tech support person
    return render(request,
                  'show_techsupport_person.html', {
                                     "person": person,
                                     })


# LIST all Tech Support people
def all_techsupport_people(request):
    """ call all PeopleTechSupport objects from models.py """
    people = PeopleTechSupport.objects.all()
    # set up pagination, show 2 people per page
    p = Paginator(PeopleTechSupport.objects.all(), 6)
    # return the page
    page = request.GET.get('page')
    people_list = p.get_page(page)

    # list all tech support people
    return render(request,
                  'all_techsupport_people.html', {
                                     "people": people,
                                     "people_list": people_list,
                                    })


# CREATE (add) new Tech Support People
def add_tech_support(request):
    """ check if user is PeopleTech """
    if request.user.username != 'PeopleTech':
        return redirect('/')

    # obtain all data posted from techsupport form
    tech_support_form = TechSupportForm()
    # if user has submitted form
    if request.method == 'POST':
        tech_support_form = TechSupportForm(data=request.POST)
        # if user has permission to add a person
        if request.user.has_perm("events.add_peopletechsupport"):

            # if tech support form is valid (required fields completed)
            if tech_support_form.is_valid():
                # save to database
                new_tech_support = tech_support_form.save(commit=False)
                # pass in logged in user.id as 'owner'
                new_tech_support.ts_owner = User.objects.get(
                    id=request.user.id)
                # then save the new person
                new_tech_support.save()
                # redirect auth user back to 'all_techsupport_people' page
                return redirect(reverse('all_techsupport_people'))

            else:
                # display error message to user
                messages.warning(request,
                                 ("'Experience' allows 400 characters only"))
        else:
            # display error message to user
            messages.warning(request,
                             ("You are not authorised to add a person"))

    else:
        # return form for authorised user to complete
        return render(request, 'add_tech_support.html',
                      {'tech_support_form': tech_support_form})
