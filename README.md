# ExpenseAid

## Expense Tracking App
------------------------------------

![alt text](/static/css/readme-images/am-i-responsive.png)

Live site available [here](https://expensed.herokuapp.com/). 


-----

## Table of Contents
--------------------------------------

- [Description](#description)
- [Design](#design)
- [UX](#ux)
- [Agile Development](#agile-development)
- [Features](#features)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Author Info](#author-info)

------

## Description
---------------------------------------

ExpenseAid is a website built in Django using Python, CSS/Bootstrap and HTML. 
This is the fourth project for the Code Institute Diploma in Software Development.

The site provides role based permissions for users to interact with a central database. It includes user authentication and Full CRUD functionality for posts.

-------
## Design
-------

#### Mock-ups
---
Home page: 

The home page provides the user with a clear understanding as to the purpose of the site. The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using.

![Home Page](/static/css/readme-images/ux-home.jpg)


Posts Page:

Users have the ability to create posts to log and keep a record of. The goal of the design is to provide a simple, clear post layout that can adapt to any size device. 
Simply clicking on the post will be displayed in the form of a summary card from which the user can access the full post details. The user can also edit and delete expenses from this view.

![posts view](/static/css/readme-images/ux-post.jpg)


[Back to the Top](#table-of-contents)

Once I was happy with the overall structure of the site, I selected the images that would guide my colour scheme. I used WAVE extension to check for colour contrast issues, then confrimed with Lighthouse to ensure that the appropriate colours were used to maximise accessibility for users.


[Back to the Top](#table-of-contents)

## UX
*  ExenseAid is intended to a professional user friendly site , that is easy to navigate through - almost foolproof - of tracking money that will alter be reimbursed. The overall design of the site aim to provide the user with an enjoyable environment and experience.

### The Sites Ideal User

* An individual or company looking to keep track of expenses online so they can be logged for reimbursment.

### Site Goals

* To allow a user to log an expense.
* To provide users with a place to keep of their expenses.


[Back to the Top](#table-of-contents)

## Agile Development

The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using issues on git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks. It was prioritised using GitHub labels with different colors which were linked to the project and can be found in the project kanban board [here](https://github.com/users/KeoCode/projects/4/views/1)


### Epics

1. Sign in/out
2. Expense Post
3. Home page
4. CRUD
5. Authorisation

### User Stories

These are the user stories that were completed within the projects first release.

- User sign in or sign out
	*  User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can keep my account secure
	*  Features restricted to signed in users - As a Site Owner, I would like to restrict some features of the site to registered users, so that it encourages people to sign up to the site

- User Expense post
	*  Create a post - As a User, I would like to be able to create an expense post.
	*  View posts - As a User, I can access my posts on the site.
	*  Update a post - As a user, I can update a post that I have created, so that I can correct any mistakes I may have made
	*  Delete a post - As a user, I can delete a post that I have created, so that I can remove it from the site

- Home page
    *  As a User on the Home page I should be easily able to Log in or Register for an account

- Authorisation
	*  As the site developer I would like to restrict the CRUD functionality to logged in Users


[Back to the Top](#table-of-contents)


## Features

**Features planned:**
* User account - Create, Read, Update and Delete posts.
* Expense posts - Users can create, read, update and delete their own expense posts.
* Users can login to their account.
* Users can logout of their account.
* Users need to be registered and logged in to access any posts.
* Responsive Design - The site needs to be fully responsive to cover the wide variety of devices and browsers users may use to access the site.

![Am I Responsive](/static/css/readme-images/am-i-responsive.png)

#### Home page
The Front page asks a the visitor of the site to log into view their posts. If already logged in then it displays posts created by the user.

![Home Page](/static/css/readme-images/home-page.png)

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require.

![Nav Bar](/static/css/readme-images/navbar.png)

#### Footer
A common footer is utilised throughout the site with the brand shown on the bottom left corner. 

![footer](/static/css/readme-images/footer.png)

#### Expense post Cards
Once logged in the page shows you upto 6 post cards per screen. The cards show the user the title of the Expense, the placeholder image, the author and the Expense amount. This allows the users to quickly identify the posts they would like to look at in more detail, to edit or delete.

##### View post detail
![Example Post Card](/static/css/readme-images/post-sample.png)

#### User Account
Users can also access their own posts easily.

![Easy Access to view posts](/static/css/readme-images/home-page.png)

#### Edit the post
Users can select a post to edit the title, date, amount or content which when selected it auto populates the saved values. Once saved the edit you get an alert confirming the post has been successfully edited.

![Easy Access to edit posts](/static/css/readme-images/edit-post.png)
![Confirmation of edit of post](/static/css/readme-images/confirm-edit.png)

#### Delete the post
Users can select a post to delete the post completely in which it will bring you to page to secondary page to confirm that you want to delete this post.

![Easy Access to view posts](/static/css/readme-images/confirm-delete.png)

## Future Enhancements
There are several items of functionality that I would like to add in the future. 
The key areas I would like to add to the site in the future are:

* The ability for users to filter the posts by date
* Forgot/reset password functionality
* The ability to upload a image of the reciept to attach to a post.
* The ability to send data to a third person eg send the posts made for the month of February to the companys accountant to be able to process for payroll.


[Back to the Top](#table-of-contents)

## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site.

#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.


#### Validator Testing
All code files were validated using suitable validators for the specific language.
HTML & CSS code passed the validation.
There is no JavaScript code to be validated.
Python meets with Pep8 standards except 
* Settings.py - Line 153 - line too long- by one character and to break up the line would make readbality worse.
* Models.py - Lines 28 and 29- line too long- as you can see i tried to break it up as much as possible without effecting the readability.
All validation screenshots are included below.

All HTML and CSS validation returned the same result so I have included only 1 screenshot here.
![HTML Validation](/static/css/readme-images/html-validator-index.png)
![CSS Validation](/static/css/readme-images/css-validator.png)
![PEP8 Validation](/static/css/readme-images/python-linter-pass.png)


#### Lighthouse Testing
Below you can see the results of Googles Lighthouse Testing.

![Lighthouse Testing](/static/css/readme-images/lighthouse-score-index.png)


#### Python Testing
All Custom Python code was manually tested multiple times during and after development.

## Testing User Stories

------
User Story:

> Create a User Account - As a User, I would like to be able to create an account, so that I can create and save posts

Acceptance Criteria:
* Given that I am an unregistered user, When I am on the homepage, Then I can see a button to sign up, And, When I click on the button, Then I am taken to the user registration page.
* Given that I am an unregistered user and I am on the user registration page, When I enter my username, email address and password, And, I click on the register button, Then The system creates me an account, And, signs me in.
* Given that I have an account and I am signed into the account, When I have an option to create a post, And, when I click on that option, Then I am taken to a page where I can provide the details of my post.

Implementation of tests:
* Check for clearly accessible call to action on homepage to register for an account and that it works as expected.
* Clearly accessible link to login or register within main navigation bar and that it functions correctly.
* Easy to use User registration process, user account and profile is created upon submission.
* Clear UX design, prevent unnecessary links to register as a user, if user is already logged in.

All Tests Passed &#x2611;
---

-----

User Story:

> User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can keep my account secure.

Acceptance Criteria:
* Given that I am a registered user, who is not logged in when I navigate to the sign in page and I enter my credentials correctly and press sign in then I am signed into my account.
* Given that I am a registered user, who is currently logged in when I click on the sign out link then I am signed out of my account.
* Given that I am a registered user, who has signed out of my account when I use the browser navigation buttons such as back button then I can not access information which requires me to be signed in.

Implementation of tests:
* Provide login and logout functionality.
* Secure restricted pages from access when a user is not signed in.

All Tests Passed &#x2611;
---

-----

User Story:

> Features restricted to signed in users - As a Site Owner, I would like to restrict some features of the site to registered users, so that it encourages people to sign up to the site.

Acceptance Criteria:
* Given that a user is not registered or signed in, when they look at a post then they do not have the ability to create a post.
* Given that a user is not registered or signed in, when they look at a post then they are unable to leave a comment.
* Given that a user is not registered or signed in, when they encounter functionality that requires them to be signed in then they are redirected to the login or register page.

Implementation of tests:
* Restrict the ability to create a post to authenticated users.
* Restrict the ability to comment on posts to authenticated users.
* Redirect users who make a request for functionality that requires them to be authenticated users to the login page

All Tests Passed &#x2611;
---

-----

User Story:

> Create a post
 - As a User, I would like to be able to create a post to be able keep a log for future review.

Acceptance Criteria:
* Given that I am a logged in user when I navigate to the 'Add Expense Post' of the home page so I have the option to create a post.
* Given that I have created a post as a logged in user when I save the completed post then it is available to other users to view.

Implementation of tests:
* Provide authenticated users with a clear option to create a post.
* Make saved posts available to other users to view.

All Tests Passed &#x2611;
---

-----

User Story:

> View posts - As a User, I can access the posts on the site, so that I can follow them at home.

Acceptance Criteria:
* Given that I am a user on the site when I navigate to the home page then I am presented with a list of the posts i have previously created.
* Given that I am a user on the site when I navigate to the home page And When I click on a post then I am presented with the full post details.

Implementation of tests:
* Provide users of the site with the ability to access all userd posts.
* Provide users of the site with the ability to access the full post details from the post summary card.

All Tests Passed &#x2611;
---

-----

User Story:

>  Update a post
 - As a user, I can update a post that I have created, so that I can correct any mistakes I may have made.

Acceptance Criteria:
* Given that I am a registered user who has created posts when I navigate to my home page then I have the option to edit the details of my posts.

Implementation of tests:
* Provide easy access to post owners to edit posts.
* Prevent other users from editing a post they did not create.
* Provide a method for post owners to edit the post details.
* Ensure post edits are saved to the database and users are informed of changes.

All Tests Passed &#x2611;
---

-----

User Story:

> Delete a post
 - As a user, I can delete a post that I have created, so that I can remove it from the site.

Acceptance Criteria:
* Given that I am a registered user who is logged in, and has created a post when I navigate to my post then I have the option to delete that post.
* Given that I am a registered user who is logged in and wishes to delete a post, when I click the delete post button then I receive a confirmation window to confirm that I really want to delete the post.

Implementation of tests:
* Provide post owners with the option to delete their post.
* Provide post deletion requests with a confirmation window to prevent mistakes.
* Ensure confirmed deletion requests are processed on the database correctly.
* Prevent unauthorised access to post deletion functionality.
* Have Comfirmation that post has successfully been deleted

All Tests Passed &#x2611;
---

-----

User Story:

> Responsive Templates - As a Site Owner, I would like my site to be fully responsive, so that Users accessing the site from different devices have an enjoyable experience.

Acceptance Criteria:
* Given that I am a user accessing the site on my smartphone when I navigate through the site then all pages should be formatted to my device.
* Given that I am a user accessing the site on my tablet when I navigate through the site then all pages should be formatted to my device.
* Given that I am a user accessing the site on my laptop when I navigate through the site then all pages should be formatted to my device.
* Given that I am a user accessing the site on my desktop computer when I navigate the site then all pages should be formatted to suit my screen size.

Implementation of tests:
* Provide users with a fully responsive site that responds to mobile, tablet, laptop and desktop sized devices.


All Tests Passed &#x2611;
---

-----

User Story:

> Pagination, As a user only a limited number of posts/profile should be visible on any given page and I should be provided with easy navigation links to move to next/previous page.

Acceptance Criteria:
* Given that I am a User I can see buttons to navigate through the page results.
* Given that I am a User when I click on these buttons I am taken to the correct page.

Implementation of tests:
* Pagination buttons are clearly visible at the bottom of the home page.
* When Clicked these buttons take the user to the desired page.
* 6 items are shown per page, this number works well across different devices, I.E Mobile = 1 column with 6 Items, Tablet = 2 columns with 3 items each, Desktop = 3 columns with 2 items each.


All Tests Passed &#x2611;
---

[Back to the Top](#table-of-contents)

-----

## Bugs

- When implementing the ability to only view post the author created and no other users posts, with the help of student tutoring we createda class based view to handle it but  still had an issue with if there was no posts created by the user then i would just show a blank screen. Instead i wanted it to show, a message asking them to log in.
I resolved this issue by adding the class based view and editing the loop in my html template instead.
I then had the issue that if

- I had an issue adding the bars icon on the navbar, with the help of my mentor i realised i was using an outdated icon name.

- I had many other smaller errors that i was able to figure out the majority with googling with stackoverflow or youtube, also student tutoring when i felt i was spinning a web of errors and was unsure if i was heading in the right direction or spiraling deeper in the wrong direction.

[Back to the Top](#table-of-contents)

-----

## Technologies

* Python
* Django
    * Django was used as the main python framework in the development of this project.
* Heroku
    * Was used as the cloud based platform to deploy the site on.
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* Bootstrap 5
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to the Navvar bars icon for the navigation bar menu.
* CSS
    * CSS was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* Gitpod was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project

#### Resources Used

* The Django and Bootstrap documentation was used extensively during development of this project
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* Other Resourses we used to help debug and to learn new features not yet covered in the course - Youtube, StackOverflow, GeekForGeeks and Slack.


[Back to the Top](#table-of-contents)

----

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Expensed](https://dashboard.heroku.com/apps/expensed)

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    * Log into GitHub or create an account.
    * Locate the repository at https://github.com/KeoCode/expense-aid
    * At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/KeoCode/expense-aid
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine


[Back to the Top](#table-of-contents)

-----

## Credits

All Images used across the site were sourced from either pexels.com, freely available images.
The Navbar bars Icon was taken from font awesome.

I found inspiration for certain parts of my ReadMe from Previous ReadMe's to ensure It was thorough and well explained.
I relied heavily on the Code institute course work, particularly the Django walk through projects.
Further information was learned from several walk through projects available freely on youtube and websites like stackoverflow and geekforgeeks etc.

-----

## Acknowledgements

I would like to acknowledge the help and support given by my mentor, Tutor support and student care while working on this project.
Everybody on Slack for asking the questions before i thought of them and helping point out issues for me to correct.

-----


## Author Info

Sarah Keohane, Aspiring Full Stack Software Developer.
- [GitHub](https://github.com/KeoCode)
- [Linkedin](https://www.linkedin.com/in/sarah-keohane/)
- [Heroku](https://dashboard.heroku.com/apps/expensed)


[Back to the Top](#table-of-contents)