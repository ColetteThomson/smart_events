# smartevents Workforce Management Platform (WMP)

## Purpose
This website has been developed to run within an organisation's intranet and is therefore intended for internal company use and not meant to be an interface to the business' customers.  The smartevents' Workforce Management Platform (WMP) helps organisations to plan, manage and track their project teams, allowing best optimisation of the business' human capital. WMP is a permissions based system, ensuring that the correct person has access to relevant features within WMP.  WMP also offers a Chat service, encouraging all project team members to add their ideas or suggestions on the different projects.

## High level overview of registered user roles and permissions within WMP:
*Note:  All users (with the exception of unregistered users) will need to be set up with appropriate permissions by the superuser Admin.  All users will have read-only access to the Home page (landing page).*

* **Superuser (Admin)** - has full CRUD (create, read (view), update, delete) from the admin panel (and read-only from the website), across all Projects, Project Administration and Project Technical Support resources.  Admin is the only user able to create Posts (via the admin panel) on the WMP Chat, and approve (publish) project team member's posted ideas and suggestions.
* **Project Manager** (PM) - will have full CRUD capability on all projects created by themselves. In addition, they will have read-only access to all project human resources (Administration staff and Technical Support staff), so that they may select appropriate team members for their project based on market experience and employee availability.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* **Administration People Owner** (APO)- will have full CRUD capability on all project Administration resources and are therefore responsible for keeping WMP up to date as regards employee availability and updating of current project experience.  In addition, the APO will have read-only access to all projects and all technical support resources, to enable them to provide accurate recommendations of appropriate team members should the PM or Technical Support People Owner (TSPO) require their input or advice.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* **Technical Support People Owner** (TSPO) - will have full CRUD capability on all project Technical Support resources and are therefore responsible for keeping WMP up to date as regards employee availability and updating of current project experience.  In addition, the TSPO will have read-only access to all projects and all project administration resources, to enable them to provide accurate recommendations of appropriate team members should the PM or APO require their input or advice.  For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.
* **General Users** - these will be project team members who have read only access to all Projects and all project human resources (Administration staff and Technical Support staff). For the Chat Posts - they will have read-only access to the content of the Post, and will be able to add (create) any ideas or suggestions they may have to individual posts.

#### Unregistered Users
* Will have read-only access to the Home Page and the different Chat Posts with any already published ideas or suggestions.  They are unable to add any ideas or suggestions to Posts and do not have any access to projects or people resources present on the WMP.

## The smartevents WMP website pages are as follows:
* **Home** (index.html): landing page
* **Chat**: opens the 'All Project Posts' page. <br>
The page: Individual post detail (i.e. 'Project Name...') can then be accessed via the chosen post from 'All Project Posts' page.
* **Projects**: dropdown reveals:  'Search Projects'; 'All Projects'; 'Add Project'. <br>
The pages: 'Project Details'; 'Update Project' and the 'Delete Project button' can be accessed from 'All Projects' (permission-based). The 'Add Project' page is also permission-based.
* **Admin People**: dropdown reveals:  'Search Admin People'; 'All Admin People'; 'Add Admin People'.<br> 
The pages: 'Personal Details'; 'Update Administration Person' and the 'Delete Person button' can be accessed from 'All Administration People' (permission-based). The 'Add Admin People' page is also permission-based.
* **Tech People**: dropdown reveals:  'Search Tech Support People'; 'All Tech Support People'; 'Add Tech Support People'.<br> The pages: 'Personal Details'; 'Update Tech Support Person' and the 'Delete Person button' can be accessed from 'All Tech Support People' (permission-based). The 'Add Tech Support People' page is also permission-based.
* **Logout**: visible when users are logged in
* **Login**: visible when users are logged out
* **Register**: visible when users are logged out

The live project can be found [here](https://smart-events.herokuapp.com/)

## Entity Relationship Diagram (ERD) for smartevents WMP
There are six models within the smartevents WMP website:<br>
* django.contrib.auth User model
* Post
* Comment
* Project
* PeopleAdministration
* PeopleTechSupport

The ERD showing the relationship between models on the smartevents WMP website can be found [here](/smartevents/images/smartevents-WMP_ERD.jpg). <br>

## Wireframes for smartevents WMP

### HOME app
[Home page](/smartevents/images/wf_home_homepage.jpg). <br>

### CHAT app
[All Project Posts](/smartevents/images/wf_chat_all-project-posts.jpg). <br>
[Project Name... (post detail page)](/smartevents/images/wf_chat_individual-post.jpg). <br>

### EVENTS app
**Projects :**<br>
*without/no permissions :*<br>
[Search Projects](/smartevents/images/wf_events_search-projects.jpg). <br>
[All Projects](/smartevents/images/wf_events_all-projects_np.jpg). <br>
[Project Details](/smartevents/images/wf_events_project-details_np.png). <br>

*with permissions :*<br>
[All Projects (with permissions)](/smartevents/images/wf_events_all-projects.jpg). <br>
[Add Project (with permissions)](/smartevents/images/wf_events_add-project.jpg). <br>
[Project Details (with permissions}](/smartevents/images/wf_events_project-details.jpg). <br>
[Update/Delete Project (with permissions)](/smartevents/images/wf_events_update-project.jpg). <br>

**Administration People :**<br>
*without/no permissions :*<br>
[Search Admin People](/smartevents/images/wf_events_search-admin-person.jpg). <br>
[All Admin People](/smartevents/images/wf_events_all-admin-people_np.jpg). <br>
[Personal Details - Admin](/smartevents/images/wf_events_personal-details-admin_np.png). <br>

*with permissions :*<br>
[All Admin People (with permissions)](/smartevents/images/wf_events_all-admin-people.jpg). <br>
[Add Admin People (with permissions)](/smartevents/images/wf_events_add-admin-person.png). <br>
[Personal Details - Admin (with permissions}](/smartevents/images/wf_events_personal-details-admin.jpg). <br>
[Update/Delete Admin Person (with permissions)](/smartevents/images/wf_events_update-admin-person.jpg). <br>

**Technical Support People :**<br>
*without/no permissions :*<br>
[Search Tech Support People](/smartevents/images/wf_events_search-tech-people.jpg). <br>
[All Tech Support People](/smartevents/images/wf_events_all-tech-people_np.jpg). <br>
[Personal Details - Tech Support](/smartevents/images/wf_events_personal-details-tech_np.jpg). <br>

*with permissions :*<br>
[All Tech Support People (with permissions)](/smartevents/images/wf_events_all-tech-people.jpg). <br>
[Add Tech Support People (with permissions)](/smartevents/images/wf_events_add-tech-person.jpg). <br>
[Personal Details - Tech Support (with permissions}](/smartevents/images/wf_events_personal-details-tech.jpg). <br>
[Update/Delete Tech Support Person (with permissions)](/smartevents/images/wf_events_update-tech-person.jpg). <br>

### ACCOUNT pages:<br>
[Log In](/smartevents/images/wf_account-login.jpg). <br>
[Log Out](/smartevents/images/wf_log-out.jpg). <br>
[Register](/smartevents/images/wf_account-register.jpg). <br>

### Unregistered Users:<br>
[Home Page](/smartevents/images/wf_non-registered-user_home.jpg). <br>
[All Project Posts](/smartevents/images/wf_non-registered-user_all-project-posts.jpg). <br>
[Project Name... (post detail page)](/smartevents/images/wf_non-registered-user_individual-post.jpg). <br>

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

## Structural Features of the smartevents WMP website

### Website Responsiveness
* Bootstrap and CSS @media queries have been used to ensure the website is viewable across laptops/desktops, tablets and mobile phones. The size and layout of text content, backgrounds and images will all adapt according to the viewing device to ensure readability and quality.
* All features on each web page are fully accessible and responsive across all viewing devices (laptops/desktops, tablets and mobile phones). 
* This feature fulfills the user story: *'As a new user, I want to be able to view the website on all device types'*. 

### Navigation Options
* This feature is intended to enable the user to quickly and easily navigate between web pages without having to utilise the browser 'back' button.
* Present on all 21 pages of the website, the fully navigational links - on the top of each page (menu links) and/or in the body of the page (hyperlinks or buttons) - will provide access to other pages in the website.
* Clicking on the 'WMP' in the navigation bar (at the top of each page) will return the user to the home page.
* This feature fulfills the user stories: *'As a new user, the navigational layout must be easy to understand and follow'* and *'As a new user, I want information on what services they offer'*.

### Footer Element
* Present on all 21 pages of the website, the footer contains copyright information and navigational links to the social media accounts of smartevents WMP.
* This feature fulfills the user stories: *'As a new user, I want information on what services they offer'*.

# Details of smartevents WMP Web Pages
**NB**: *Unfortunately the smartevents WMP website will not display in the 'amiresponsivedesign.is' website. Therefore, screenshots of individual pages have been provided instead. Note: all website pages have been tested (and passed) for responsive design as per the test cases.*<br>

## 1.  The 'Home' app: index.html (Home page or Landing page)

This page is intended to provide:
* an at-a-glance view of the main purpose of the website, i.e. a Workforce Management Platform (WMP) to help project managers and their teams select the right resource for the right task - and - the availability of a project Chat to encourage project team member interaction and participation.
* an at-a-glance high level view of the different WMP roles and permissions, so that potential users can immediately see what user options are available.
* contact details (email and phone) for the website Administrator, so that users can request to be set up as a registered website user
* This feature fulfills the user stories: *'As a new user, I want to immediately understand the main purpose of the website'* and *'As a new user, I want information on what services they offer* and *'As a new user, I want to be able to easily contact the organisation'* and *'As a new user, I want to register for an account, so that I can access appropriate website content'* and *'As a new user, I want to understand what access I have to what website content'* and *'As a new user, the navigational layout must be easy to understand and follow'*.

A screenshot of the 'Home' page (index.html) can be found [here](/smartevents/images/mu_home_perm.jpg). <br>

## 2.  The Chat app pages: 'All Project Posts' page and 'Project Name...' page

The **All Project Posts** page is intended to provide:
* a list of all the organisation's active projects.
* details of each active project listed can be accessed by clicking either the project name (eg Project 1...) or the slug (eg: energy consumption...).
* the author (i.e. the Administator) is displayed above the project name.
* the date and time the Post was created and the current amount of 'likes' for that particular project.
* This feature fulfills the user stories: *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want to be able to view all the organisation's active projects in the Chat'*

*without/no permissions :*<br> 
A screenshot of the 'All Projects Posts' page can be found [here](/smartevents/images/mu_all-project-posts_np.jpg). <br>

The **Project Name...** page is intended to provide:
* the active project's name, its author and created date and time of the post.
* an 'overview' of the project specification.
* requested ideas/suggestions for the project.
* indication of the amount of likes (heart) and published ideas/suggestions (speech bubbles) for the project.
* a 'body' box (bottom right of page) for registered users to add their idea/suggestion, and an accompanying submit button.
* approved (published) ideas/suggestions (bottom left of page) detailing: the author, date and time of creation and content of submitted post.
* user messaging: should a user submit an idea/suggestion, a flash message will appear informing the user their submission is awaiting approval.  All Chat post submissions will need to be authorised (published) by the Administrator.
* This feature fulfills the user stories: *'As a returning user, I want to be able to view all the organisation's active projects in the Chat'* and *'As a returning user, I want to be able to add my ideas or suggestions on the different Project Posts'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*without/no permissions :*<br> 
A screenshot of the 'Project Name...' page can be found [here](/smartevents/images/mu_project-name_np.jpg). <br>

*with permissions :*<br> 
A screenshot of the 'Project Name...' page can be found [here](/smartevents/images/mu_project-name_perm.jpg). <br>

## 3.  Dropdowns for 'Projects'; 'Admin People' and 'Tech People'

* **Projects dropdown**: 'Search Projects'; 'All Projects'; 'Add Project' pages
* **Admin People dropdown**: 'Search Admin People'; 'All Admin People'; 'Add Admin People' pages
* **Tech People dropdown**: 'Search Tech Support People'; 'All Tech Support People'; 'Add Tech Support People' pages

The three **Search...** pages are intended to provide:
* a search bar for users to enter their criteria (this field is case sensitive).
* a 'search' button to submit their criteria.
* a confirmation of the user's submitted search (i.e. you searched for ...).
* a listing of linked matches to the user's criteria should their search be successful.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'*.

*without/no permissions :*<br> 
A screenshot of the 'Search Projects' page can be found [here](/smartevents/images/mu_search-projects_np.jpg). <br>
A screenshot of the 'Search Admin People' page can be found [here](/smartevents/images/mu_search-admin-people_np.jpg). <br>
A screenshot of the 'Search Tech Support People' page can be found [here](/smartevents/images/mu_search-tech-people_np.jpg). <br>

The three **All...** pages are intended to provide:
* depending on the chosen page, a listing of: 'all projects' OR 'all admin people' OR 'all tech support people' - that are present in the WMP database.
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view a listing of: 'all projects' OR 'all admin people' OR 'all tech support people'.
* pagination showing page number and number of pages.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'*.

*without/no permissions :*<br> 
A screenshot of the 'All Projects' page can be found [here](/smartevents/images/mu_all-projects_np.jpg). <br>
A screenshot of the 'All Admin People' page can be found [here](/smartevents/images/mu_all-admin-people_np.jpg). <br>
A screenshot of the 'All Tech Support People' page can be found [here](/smartevents/images/mu_all-tech-people_np.jpg). <br>

*with permissions :*<br> 
A screenshot of the 'All Projects' page with permissions can be found [here](/smartevents/images/mu_all-projects_perm.jpg). <br>
A screenshot of the 'All Admin People' page with permissions can be found [here](/smartevents/images/mu_all-admin-people_perm.jpg). <br>
A screenshot of the 'All Tech Support People' page with permissions can be found [here](/smartevents/images/mu_all-tech-people_perm.jpg). <br>

The three **Add...** pages are intended to provide:
* depending on user permissions: the display of an empty form for the user to: 'add a new administration person' OR 'add a new technical support person' OR 'add a new project'.
* a 'submit' button to confirm the user's entry of the completed form.
* user messaging: confirmation that the user has: 'added a new administration person' OR 'added a new technical support person' OR 'added a new project'.
* This feature fulfills the user stories: *' As a returning user, I want to be able to create (add) new content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*with permissions :*<br>
A screenshot of the 'Add Project' page can be found [here](/smartevents/images/mu_add-project_perm.jpg). <br>
A screenshot of the 'Add Admin People' page can be found [here](/smartevents/images/mu_add-admin-person_perm.jpg). <br>
A screenshot of the 'Add Tech Support People' page can be found [here](/smartevents/images/mu_add-tech-person_perm.jpg). <br>

### 'Personal Details' pages for 'Admin People' and 'Tech People'
Note: these pages become accessible when clicking the 'person name...' from either the 'All Admin People' page OR the 'All Tech Support People' page.

The two **Personal Details** (**show_admin_person** and **show_techsupport_person**) pages are intended to provide:
* an overview of an individual person's details. 
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view the personal details overview of: 'Admin person' OR 'Tech Support person'.
* user messaging: confirmation of 'updating' or 'deleting' of a person.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*without/no permissions :*<br> 
A screenshot of the 'Personal Details' page (from 'All Admin People') can be found [here](/smartevents/images/mu_personal-details-admin_np.jpg). <br>
A screenshot of the 'Personal Details' page (from 'All Tech Support People') can be found [here](/smartevents/images/mu_personal-details-tech_np.jpg). <br>

*with permissions :*<br>
A screenshot of the 'Personal Details' page with permissions(from 'All Admin People') can be found [here](/smartevents/images/mu_personal-details-admin_perm.jpg). <br>
A screenshot of the 'Personal Details' page with permissions (from 'All Tech Support People') can be found [here](/smartevents/images/mu_personal-details-tech_perm.jpg). <br>

### 'Project Details' page for 'Projects'
Note: this page becomes accessible when clicking the 'project name...' from the 'All Projects' page.

The **Project Details** (**show_project**) page for 'Projects' is intended to provide:
* an overview of an active project's details. 
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view the project details overview of: 'Project Name....
* user messaging: confirmation of 'updating' or 'deleting' of a project.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*without/no permissions :*<br> 
A screenshot of the 'Project Details' page (from 'All Projects') can be found [here](/smartevents/images/mu_project-details_np.jpg). <br>

*with permissions :*<br>
A screenshot of the 'Project Details' page with permissions (from 'All Projects') can be found [here](/smartevents/images/mu_project-details_perm.jpg). <br>

### 'Update...' pages and 'Delete...' button for 'Projects', 'Admin People' and 'Tech Support People'
Note: this page is permission-based and becomes accessible when clicking the 'project name...' from the 'All Projects' page OR the 'person name...' from the 'All Admin People' OR 'All Tech Support People' pages.
This page is also accessible from the 'Personal Details' and 'Project Details' pages.

The **Update...** pages are intended to provide:
* a pre-populated form with existing information on: 'Projects' OR 'Admin People' OR 'Tech Support People'.
* an 'update...' button to confirm the user's changes to the existing form information.
* user messaging: confirmation of the 'updating' of a project's details OR a person's details.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

The **Delete...** button (next to the 'update' button)
Note: this button is permission-based and is accessible from the 'All Projects' page OR the 'All Admin People' page OR the 'All Tech Support People' page. This button is also accessible from the 'Personal Details' and 'Project Details' pages.
* a 'delete...' button to confirm the user's decision to delete: a 'project' from 'All Projects' OR a 'person' from 'All Admin People' OR 'All Tech Support People' pages.
* user messaging: confirmation of the 'deleting' of a project's details OR a person's details.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and '*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*with permissions :*<br>
A screenshot of the 'Update Project' page (from 'Projects') can be found [here](/smartevents/images/mu_update-project_perm.jpg). <br>
A screenshot of the 'Update Person' page (from 'Admin People') can be found [here](/smartevents/images/mu_update-admin-person_perm.jpg). <br>
A screenshot of the 'Update Person' page (from 'Tech People') can be found [here](/smartevents/images/mu_update-tech-person_perm.jpg). <br>

## 4.  'Logout'; 'Login' and 'Register' pages

These pages are intended to provide:
* Logout - confirmation to a registered user that they want to logout
* Login - request of login information (username and password) from registered users
* Register - request of user information (username, password, re-type password, optional email) from new users

A screenshot of the 'Logout' page can be found [here](/smartevents/images/mu_logout_np.jpg). <br>
A screenshot of the 'Login' page can be found [here](/smartevents/images/mu_login_np.jpg). <br>
A screenshot of the 'Register' page can be found [here](/smartevents/images/mu_register_np.jpg). <br>

## Design of the smartevents WMP website

### Colour Scheme
The colour palette for general body content comprises four basic colours: 
* #445261 (medium grey) - body text; footer elements
* #038bfa (blue) - logo and branding; headings; button text
* #202020 (dark grey) - body text; update button text
* whitesmoke - update and delete buttons; button background; delete button text; links

The colour palette for the four user-type roles comprises four basic colours:
* project manager: #fa03fa (pink)
* admin people owner: #8c9b0c (lime green)
* tech people owner: #c48a0d (orange)
* general user: #3a3a3a (grey)

### Fonts
The 'smartevents' logo uses **Lato**; the 'WMP' brand uses **Permanent Marker**; and body text and headings use **Roboto**.  The back-up font is **sans-serif** for Lato and Roboto and **cursive** for Permanent Marker.  Fonts were downloaded from **Google Fonts**.

### Imagery
Images for the website have been downloaded from **Pexels** and are stored in **Cloudinary**.

### Limitations
No known limitations.

## Features
* Login, Logout and Register user account functionality
* Blog capability (Chat) - users are able to add comments and like project posts. Superuser (Administrator) is able to create posts
* Full CRUD (create, read, update, delete) functionality that is permissions- and role-based
* Similar 'look-and-feel' across different user roles (example: all search screens have the same basic appearance) - this is to enhance the user experience and allow for quick familiarisation of the WMP system
* Colour-coded user roles - for ease of use and to enhance the user experience
* Messaging system confirming user actions on the website
* Different page views depending on a user's role and permissions
* Home page provides at at-a-glance reminder of the different user roles

## Technologies
* Django - a framework that follows the model–template–views architectural pattern and upon which this website is built
* Python - website functionality enhanced by custom written Python
* HTML - the structure of this website project uses custom written HTML as the main language
* Bootstrap - utilised mostly for website responsiveness
* CSS - the styling of this website encompasses custom written CSS
* Javascript - website interaction provided by custom written Javascript
* [Google Fonts](https://fonts.google.com/) - utilised for the logo, brand and body text
* [FontAwesome](https://fontawesome.com/) - utilised for Chat app icons
* [GitHub](https://github.com/) - hosting site for storage of source code for the website and [Git Pages](https://pages.github.com/) for the deployment of the website
* [Git](https://git-scm.com/) - used as version control software to commit and push code to a GitHub repository where all source code is located
* [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - these are built in developer tools used to inspect page elements (eg. responsive design; debug issues; testing of different CSS styling options; and the Lighthouse Reports
* [Pexels](https://www.pexels.com/) - Chat image for smartevents WMP website
* [Cloudinary](https://cloudinary.com/) - cloud storage of Chat image for smartevents WMP website; serve static files
* [PicPick](https://picpick.app/en/) - used to create screenshots of smartevents WMP Website pages
* [Heroku](https://www.heroku.com/) - final project (website) deployed to and stored on Heroku

## Testing
* Manual testing has been performed to check for back-end functionality (Django, Python, Javascript), as well as visual effects and website layout (HTML, Bootstrap, CSS).
* Testing has been performed to check for compatibility across three web browsers (Google Chrome, Firefox, Opera).
* Responsive design has been tested across the different screen sizes: desktops/laptops (1024px); tablets (max-width 769px); mobiles (to a max-width of 426px); and large laptops (min-width 1025px to max-width 1441px).
* All navigational links should direct to the correct html web page as per their names.<br>
Exceptions: the 'Home' page, will direct to 'index.html'; the 'show_admin_person.html' and 'show_techsupport_person.html' will direct to 'Personal Details'; the 'show_project' will direct to 'Project Details'. 

### Test Cases
* Test cases can be found here for the **index.html** (home) and base.html: <br> 
[Home app and base.html](/smartevents/images/testcases_home_base.jpg)
* Test cases can be found here for the **Chat** app pages (post_list.html | post_detail.html) : <br> 
[Chat app](/smartevents/images/testcases_chat-app.jpg)<br>
* Test cases can be found here for the various **Events** app pages (add... | update... | delete... | view... ): <br>
[Events app](/smartevents/images/testcases_events-app.jpg).
* Test cases can be found here for the **Logout, Login, Register** and **un-registered users** pages: <br>
[Accounts pages](/smartevents/images/testcases_accs-pages.jpg).

### Testing Issues and Resolutions
The following issue arose during HTML validation with the 'Chat' app's 'post_detail.html' page:
* the code for the page works as expected and the page is responsive
* the page however failed the html validation (due to unexplained <o:p></o:p> tags). Through extensive research and some consultation with Tutor Support - I have been able to resolve this code validation issue (through the removal of 'Summernote') - so that it eventually passed the HTML validation.

## Code Validation
All 21 HTML pages were run through the [W3C Markup Validation Service](https://validator.w3.org/) and showed no errors. The following web pages were checked: 
* Home app: index.html page
* Chat app: 'post_list' | 'post_detail<br>
[HTML: Home and Chat app pages](/smartevents/images/html_validation_home-app_chat-app.jpg).<br>

* Events app: 3 x search... pages | 3 x all... pages | 3 x add... pages | 3 x 'update....' pages | 3 x 'delete...' buttons | 2 x 'personal details' pages | 'project detail' page <br> 
[HTML: Events app pages](/smartevents/images/html_validation_events-app.jpg).<br>

* The CSS stylesheet was run through the [CSS Validation Service-Jigsaw](https://jigsaw.w3.org/css-validator/) and showed no errors. <br>
[CSS validation](/smartevents/images/css_validation.jpg).<br>

* The Javascript file was run through the [JSHint Validation Service](https://jshint.com) and showed no errors.<br>
[JS validation](/smartevents/images/JSHint_code-validation.jpg).<br>

## Lighthouse Reports
* Home app: index.html page
* Chat app: 'post_list' | 'post_detail<br>
[Lighthouse: Home and Chat apps](/smartevents/images/lighthouse_home-app_chat-app.jpg).<br>

* Events app: 3 x search... pages | 3 x all... pages | 3 x add... pages | 3 x 'update....' pages | 3 x 'delete...' buttons | 2 x 'personal details' pages | 'project detail' page <br> 
[Lighthouse: Events app pages](/smartevents/images/lighthouse_events-app.jpg).<br>

## Deployment
### Project Creation
The project was created using GitHub and choosing a new repository.<br>
The following terminal commands were used during this project:
* git add . - this command adds a change in the working directory to the staging area.
* git commit -m "*message*" - this command details the change/s made in the 'message' section and then commits the changes to the local repository.
* git push - this command is used to push all changes to the GitHub repository.
* Final deployment of the website is on [Heroku](https://smart-events.herokuapp.com/)

### Using GitHub Pages
* Navigate to the GitHub repository [smartevents WMP](https://github.com/ColetteThomson/smartevents_WMP).
* Select 'Settings'.
* Scroll down to 'GitHub Pages'.
* Select 'Main' branch as the source and click 'Save' button.
* Select link to go to live published page.

## Credits
### Code
* The private collaboration and knowledge sharing SaaS platform [Stack Overflow](https://stackoverflow.com/) was an invaluable resource for general coding queries.
* Use was made of Code Institute tutor support for help with persistent coding issues.
* Ideas for the Chat app was taken from Code Institute's Blog videos.

### Content
* Inspiration was taken from the need for a simple workforce management tool.
* Ideas for project content were taken from the website [Springboard Worldwide](http://springboardww.com/index.php/demand-generation/previous-project-examples) and [Stanford Education](http://web.stanford.edu/class/msande108/handouts/PastServe.pdf).
