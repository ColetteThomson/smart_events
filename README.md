# smartevents Workforce Management Platform (WMP)

## Purpose
This website has been developed to run within an organisation's intranet and is therefore intended for internal company use and not intended to be an interface to the business's customers.  The smartevents' Workforce Management Platform (WMP) helps organisations to plan, manage and track their project teams, allowing best optimisation of the business' human capital. WMP is a permissions based system, ensuring that the correct person has access to relevant features within WMP.  WMP also offer a Chat service, encouraging all project team members to add their ideas or suggestions on the different projects.

### High level overview of registered user roles and permissions within WMP:
**Note:  All users (with the exception of general users) will need to be set up with appropriate permissions by the superuser Admin.  All users will have read-only access to the Home page (index.html)**

* Superuser (Admin) - has full CRUD from the admin panel (and read-only from the website), across all Projects, Project Administration and Project Technical Support resources.  Admin is the only user able to create Posts (via the admin panel) on the WMP Chat, and approve (publish) project team member's posted ideas and suggestions.
* Project Manager (PM) - will have full CRUD (create, read (view), update, delete) capability on all projects created by themselves. In addition, they will have read-only access to all project human resources (Administration staff and Technical Support staff), so that they may select appropriate team members for their project based on market experience and employee availability.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* Administration People Owner (APO)- will have full CRUD capability on all project administration resources and are therefore responsible for keeping WMP up to date as regards employee availability and updating of current project experience.  In addition, the APO will have read-only access to all projects and all technical support resources, to enable them to provide accurate recommendations of appropriate team members should the PM or Technical Support People Owner (TSPO) require their input or advice.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* Technical Support People Owner (TSPO) - will have full CRUD capability on all project technical support resources and are therefore responsible for keeping WMP up to date as regards employee availability and updating of current project experience.  In addition, the TSPO will have read-only access to all projects and all project administration resources, to enable them to provide accurate recommendations of appropriate team members should the PM or APO require their input or advice.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* General Users - these will be project team members who have read only access to all projects and all project human resources (Administration staff and Technical Support staff). For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.

### Unregistered Users
* Will have read-only access to the Home Page and the different Chat Posts with any already published ideas or suggestions.  They are unable to add any ideas or suggestions to Posts and do not have any access to projects or people resources present on the WMP.

## The WMP website pages are as follows:
* Home (index.html): opening page
* Chat: opens the All Project Posts page.  Individual Post detail (i.e. Project Name) can then be accessed via required selection
* Projects: dropdown reveals:  Search Projects; All Projects; Add Project
* Admin People: dropdown reveals:  Search Admin People; All Admin People; Add Admin People
* Tech People: dropdown reveals:  Search Tech Support People; All Tech Support People; Add Tech Support People
* Logout: visible when users are logged in
* Login: visible when users are logged out
* Register: visible when users are logged out

The live project can be found [here](https://)

## User Experience Design

### User Stories
#### New Authorised User Usability Goals
* As a site user, I want