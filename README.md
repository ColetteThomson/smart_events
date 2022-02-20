# smartevents Workforce Management Platform (WMP)

## Purpose
This website has been developed to run within an organisation's intranet and is therefore intended for internal company use and not intended to be an interface to the business's customers.  The smartevents' Workforce Management Platform (WMP) helps organisations to plan, manage and track their project teams, allowing best optimisation of the business' human capital. WMP is a permissions based system, ensuring that the correct person has access to relevant features within WMP.  WMP also offer a Chat service, encouraging all project team members to add their ideas or suggestions on the different projects.

### High level overview of registered user roles and permissions within WMP:
*Note:  All users (with the exception of general users) will need to be set up with appropriate permissions by the superuser Admin.  All users will have read-only access to the Home page (landing page).*

* Superuser (Admin) - has full CRUD from the admin panel (and read-only from the website), across all Projects, Project Administration and Project Technical Support resources.  Admin is the only user able to create Posts (via the admin panel) on the WMP Chat, and approve (publish) project team member's posted ideas and suggestions.
* Project Manager (PM) - will have full CRUD (create, read (view), update, delete) capability on all projects created by themselves. In addition, they will have read-only access to all project human resources (Administration staff and Technical Support staff), so that they may select appropriate team members for their project based on market experience and employee availability.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* Administration People Owner (APO)- will have full CRUD capability on all project administration resources and are therefore responsible for keeping WMP up to date as regards employee availability and updating of current project experience.  In addition, the APO will have read-only access to all projects and all technical support resources, to enable them to provide accurate recommendations of appropriate team members should the PM or Technical Support People Owner (TSPO) require their input or advice.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* Technical Support People Owner (TSPO) - will have full CRUD capability on all project technical support resources and are therefore responsible for keeping WMP up to date as regards employee availability and updating of current project experience.  In addition, the TSPO will have read-only access to all projects and all project administration resources, to enable them to provide accurate recommendations of appropriate team members should the PM or APO require their input or advice.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* General Users - these will be project team members who have read only access to all projects and all project human resources (Administration staff and Technical Support staff). For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.

### Unregistered Users
* Will have read-only access to the Home Page and the different Chat Posts with any already published ideas or suggestions.  They are unable to add any ideas or suggestions to Posts and do not have any access to projects or people resources present on the WMP.

## The smartevents WMP website pages are as follows:
* Home (index.html): opening page
* Chat: opens the 'All Project Posts' page.  Individual post detail (i.e. 'Project Name...') can then be accessed via the chosen post from the 'All Project Posts' page
* Projects: dropdown reveals:  Search Projects; All Projects; Add Project
* Admin People: dropdown reveals:  Search Admin People; All Admin People; Add Admin People
* Tech People: dropdown reveals:  Search Tech Support People; All Tech Support People; Add Tech Support People
* Logout: visible when users are logged in
* Login: visible when users are logged out
* Register: visible when users are logged out

The live project can be found [here](https://)

## User Experience Design

### User Stories
#### New User Usability Goals
* As a new user, I want to immediately understand the main purpose of the website
* As a new user, I want information on what services they offer
* As a new user, I want to be able to easily contact the organisation
* As a new user, the navigational layout must be easy to understand and follow
* As a new user, I want to be able to view the website on all device types
#### New User Functionality Goals
* As a new user, I want to register for an account, so that I can access appropriate website content
* As a new user, I want to understand what access I have to what website content

#### Returning User Functionality Goals
* As a returning user, I want to have appropriate access to website content as per my permissions
* As a returning user, I want to be able to find (read/view) the information I'm looking for
* As a returning user, I want to be able to create (add) new content, as per my permissions
* As a returning user, I want to be able to edit (update) existing content, as per my permissions
* As a returning user, I want to be able to delete existing content, as per my permissions
* As a returning user, I want to be able to view all the organisation's active projects in the Chat
* As a returning user, I want to be able to add my ideas or suggestions on the different Project Posts
* As a returning user, I want confirmation of actions I have performed on the WMP website

### Structural Features of the smartevents WMP website

#### Website Responsiveness
* Bootstrap and CSS @media queries have been used to ensure the website is viewable across laptops/desktops, tablets and mobile phones. The size and layout of both text content and images will adapt according to the viewing device to ensure readability and quality.
* All features on each web page are fully accessible and responsive across all viewing devices (laptops/desktops, tablets and mobile phones). 
* This feature fulfills the user story: *'As a new user, I want to be able to view the website on all device types'*. 

#### Navigation Options
* This feature is intended to enable the user to quickly and easily navigate between web pages without having to utilise the browser 'back' button.
* Present on all 21 pages of the website, the fully navigational links - on the top of each page (menu links) and/or in the body of the page (hyperlinks or buttons) - will provide access to other pages in the website.
* Clicking on the 'WMP' in the navigation bar (at the top of each page) will return the user to the home page.
* This feature fulfills the user stories: *'As a new user, the navigational layout must be easy to understand and follow'* and *'As a new user, I want information on what services they offer'*.

#### Footer Element
* Present on all 21 pages of the website, the footer contains copyright information and navigational links to the social media accounts of smartevents WMP.
* This feature fulfills the user stories: *'As a new user, I want information on what services they offer'*.

### Details of smartevents WMP Web Pages
#### The 'Home' Page or Landing Page

A mockup of the 'Home' page (index.html) can be found [here](..). <br>

This page is intended to provide:
* an at-a-glance view of the main purpose of the website, i.e. a Workforce Management Platform (WMP) to help project managers and their teams select the right resource for the right task - and - the availability of a project Chat to encourage project team member interaction and participation.
* an at-a-glance high level view of the different WMP roles and permissions, so that potential users can immediately see what user options are available.
* contact details (email and phone) for the website Administrator, so that users can request to be set up as a registered website user
* This feature fulfills the user stories: *'As a new user, I want to immediately understand the main purpose of the website'* and *'As a new user, I want information on what services they offer* and *'As a new user, I want to be able to easily contact the organisation'* and *'As a new user, I want to register for an account, so that I can access appropriate website content'* and *'* As a new user, I want to understand what access I have to what website content'* and *'As a new user, the navigational layout must be easy to understand and follow'*.

#### The Chat pages: 'All Project Posts' page and 'Project Name...' page

A mockup of the 'All Projects Posts' page can be found [here](..). <br>
A mockup of the 'Project Name...' page can be found [here](..). <br>

The **All Project Posts** page is intended to provide:
* a list of all the organisation's active projects.
* details of each active project listed can be accessed by clicking either the project name (eg Project 1...) or the slug (eg: energy consumption...).
* the author (i.e. the Administator) is displayed above the project name.
* the date and time the Post was created and the current amount of 'likes' for that particular project.
* This feature fulfills the user stories: *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want to be able to view all the organisation's active projects in the Chat'*

The **Project Name...** page is intended to provide:
* the active project's name, its author and created date and time of the post.
* an 'overview' of the project specification.
* requested ideas/suggestions for the project.
* indication of the amount of likes (heart) and published ideas/suggestions (speech bubbles) for the project.
* a 'body' box (bottom right of page) for registered users to add their idea/suggestion, and an accompanying submit button.
* approved (published) ideas/suggestions (bottom left of page) detailing: the author, date and time of creation and content of submitted post.
* user messaging: should a user submit an idea/suggestion, a flash message will appear informing the user their submission is awaiting approval.  All Chat post submissions will need to be authorised (published) by the Administrator.
* This feature fulfills the user stories: *'As a returning user, I want to be able to view all the organisation's active projects in the Chat'* and *'As a returning user, I want to be able to add my ideas or suggestions on the different Project Posts'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

### Dropdowns for 'Projects'; 'Admin People' and 'Tech People' 
**Projects dropdown: 'Search Projects'; 'All Projects'; 'Add Project' pages**
**Admin People dropdown: 'Search Admin People'; 'All Admin People'; 'Add Admin People' pages**
**Tech People dropdown: 'Search Tech Support People'; 'All Tech Support People'; 'Add Tech Support People' pages**

A mockup of the 'Search Projects' page can be found [here](..). <br>
A mockup of the 'Search Admin People' page can be found [here](..). <br>
A mockup of the 'Search Tech Support People' page can be found [here](..). <br>

The three **Search...** pages are intended to provide:
* a search bar for users to enter their criteria (this field is case sensitive).
* a 'search' button to submit their criteria.
* a confirmation of the user's submitted search (i.e. you searched for ...).
* a listing of linked matches to the user's criteria should their search be successful.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'*.

A mockup of the 'All Projects' page can be found [here](..). <br>
A mockup of the 'All Admin People' page can be found [here](..). <br>
A mockup of the 'All Tech Support People' page can be found [here](..). <br>

The three **All...** pages are intended to provide:
* depending on the chosen page, a listing of: 'all projects' OR 'all admin people' OR 'all tech support people' - that are present in the WMP database.
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view a listing of: 'all projects' OR 'all admin people' OR 'all tech support people'.
* pagination showing page number and number of pages.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'*.

A mockup of the 'Add Project' page can be found [here](..). <br>
A mockup of the 'Add Admin People' page can be found [here](..). <br>
A mockup of the 'Add Tech Support People' page can be found [here](..). <br>

The three **Add...** pages are intended to provide:
* depending on user permissions: the display of an empty form for the user to: 'add a new administration person' OR 'add a new technical support person' OR 'add a new project'.
* a 'submit' button to confirm the user's entry of the completed form.
* user messaging: confirmation that the user has: 'added a new administration person' OR 'added a new technical support person' OR 'added a new project'.
* This feature fulfills the user stories: *' As a returning user, I want to be able to create (add) new content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

### 'Personal Details' pages for 'Admin People' and 'Tech People'
Note: these pages become accessible when clicking the 'person name...' from either the 'All Admin People' page OR the 'All Tech Support People' page.

A mockup of the 'Personal Details' page (from 'All Admin People') can be found [here](..). <br>
A mockup of the 'Personal Details' page (from 'All Tech Support People') can be found [here](..). <br>

The two **Personal Details** pages are intended to provide:
* an overview of an individual person's details. 
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view the personal details overview of: 'Admin person' OR 'Tech Support person'.
* user messaging: confirmation of 'updating' or 'deleting' of a person.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

### 'Project Details' pages for 'Projects'
Note: this page becomes accessible when clicking the 'project name...' from the 'All Projects' page.

A mockup of the 'Project Details' page (from 'All Projects') can be found [here](..). <br>

The **Project Details** page is intended to provide:
* an overview of an active project's details. 
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view the project details overview of: 'Project Name....
* user messaging: confirmation of 'updating' or 'deleting' of a project.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

### 'Update...' pages and 'Delete...' button for 'Projects', 'Admin People' and 'Tech Support People'
Note: this page is permission-based and becomes accessible when clicking the 'project name...' from the 'All Projects' page OR the 'person name...' from the 'All Admin People' OR 'All Tech Support People' pages.
This page is also accessible from the 'Personal Details' and 'Project Details' pages.

A mockup of the 'Update Project' page (from 'Projects') can be found [here](..). <br>
A mockup of the 'Update Person' page (from 'Admin People') can be found [here](..). <br>
A mockup of the 'Update Person' page (from 'Tech People') can be found [here](..). <br>

The **Update...** pages are intended to provide:
* a pre-populated form with existing information on: 'Projects' OR 'Admin People' OR 'Tech Support People'.
* an 'update...' button to confirm the user's changes to the existing form information.
* user messaging: confirmation of the 'updating' of a project's details OR a person's details.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

The **Delete...** button (next to the 'update' button)
Note: this button is permission-based and is accessible from the 'All Projects' page OR the 'All Admin People' page OR the 'All Tech Support People' page. This button is also accessible from the 'Personal Details' and 'Project Details' pages.
* an 'delete...' button to confirm the user's decision to delete: a 'project' from 'All Projects' OR a 'person' from 'All Admin People' OR 'All Tech Support People' pages.
* user messaging: confirmation of the 'deleting' of a project's details OR a person's details.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and '*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.



