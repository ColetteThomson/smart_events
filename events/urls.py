from django.urls import path
from . import views

urlpatterns = [
    # blank path to indicate default as home page
    # and render this class as a view using 'as_view()'
    # path converter if matched to return a string, if not a 404 message

    # urls paths for 'PROJECT'
    path('all_projects', views.all_projects, name='all_projects'),
    path('add_project', views.add_project, name='add_project'),
    path('show_project/<int:project_id>/', views.show_project,
         name='show_project'),
    path('update_project/<int:project_id>/', views.update_project,
         name='update_project'),
    path('delete_project/<int:project_id>/', views.delete_project,
         name='delete_project'),

    # urls paths for 'PEOPLE':  'Administration' and 'Technical Support'
    path('add_admin_people', views.add_admin_people, name='add_admin_people'),
    path('add_tech_support', views.add_tech_support, name='add_tech_support'),
    path('all_admin_people', views.all_admin_people, name='all_admin_people'),
    path('all_techsupport_people', views.all_techsupport_people,
         name='all_techsupport_people'),
    path('show_admin_person/<int:people_id>/', views.show_admin_person,
         name='show_admin_person'),
    path('show_techsupport_person/<int:people_id>/',
         views.show_techsupport_person, name='show_techsupport_person'),
    path('update_admin_people/<int:people_id>/', views.update_admin_people,
         name='update_admin_people'),
    path('update_techsupport_people/<int:people_id>/',
         views.update_techsupport_people, name='update_techsupport_people'),
    path('delete_admin_people/<int:people_id>/', views.delete_admin_people,
         name='delete_admin_people'),
    path('delete_techsupport_people/<int:people_id>/',
         views.delete_techsupport_people, name='delete_techsupport_people'),

    # urls paths for SEARCH: 'admin people', 'tech support people', 'projects'
    path('search_admin_people', views.search_admin_people,
         name='search_admin_people'),
    path('search_techsupport_people', views.search_techsupport_people,
         name='search_techsupport_people'),
    path('search_projects', views.search_projects,
         name='search_projects'),
    ]
