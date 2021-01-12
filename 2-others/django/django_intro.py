# What is Django ?
#     - It is a Web Framework - Helps you build interactive Websites using Python
#     - With Django, you define the kind of data your site needs to work with
#     - And also define the ways your users can work with that data

# Installation
#     - It’s usualy best to install Django to a virtual environment, 
#         where your project can be isolated from your other Python projects
#     - Most commands assume you’re working in an active virtual environment

#     1 - Create a virtual environment
#         python –m venv v_env
#     2 - Activate the environment
#         v_env\Scripts\activate
#     3 - Install Django to the active environment
#         (v_env)$ pip install Django

# Django Project and Apps

#     1 - Create a new project
#         django-admin.py startproject learning_log .
#     2 - Create a Database
#         python manage.py migrate
#     3 - Start a development server and View it
#         python manage.py runserver
#     4 - Create a new App - Django Project is made up of one or more Apps
#         python manage.py startapp learning_logs
    
# Working with Models
#     The data in Django project is structured as a set of Models
    
#     1 - Defining a Model
#         class Topic(models.model)
#         To define the models for your app, modify the models.py created in app's folder
#         The __str__() method tells Django how to represent data Objects based on this model
#     2 - Activating a Model
#         INSTALLED_APPS = [ "learning_logs", ] 
#         To use a model, the app must be added to the tuple INSTALLED_APPS
#         which is stored in the project’s settings.py file
#     3 - Migrating the Database
#         python .\manage.py makemigrations learning_logs
#         python .\manage.py migrate
#         The database needs to be modified to store the kind of data that the model represents
#     4 - Creating a superuser
#         python .\manage.py createsuperuser
#         A superuser is a user account that has access to all aspects of the project
#     5 - Registering a Model
#         admin.site.register(Topic)
#         You can register your models with Django’s admin site, 
#         which makes it easier to work with the data in your project
#         To do this, modify the app’s admin.py file
#         View the admin site at http://localhost:8000/admin
#     6 - Another Model
#         A new model can use an existing model
#         Foreign Key attribute establishes a connection between instances of the two related models
#         Whenever you add a new model to your app, make sure to migrate the database 
        

# Building a Simple Home Page

#     Users interact with a project through web pages, and a 
#     project’s home page can start out as a simple page with no data
#     A page usually needs a URL, a view, and a template.

#     1 - Mapping a Project's URL
#         The project’s main urls.py file tells Django
#         where to find the urls.py files associated with each app in the project
#     2 - Mapping an App's URL
#         urlpatterns = []
#         An app’s urls.py file tells Django which view to use for each URL in the app
#         You’ll need to make this file yourself, and save it in the app’s folder.
#     3 - Writing a Simple View
#         A view takes information from a request and sends data to the browser, often through a template
#         View functions are stored in an app’s views.py file
#         This simple view function doesn’t pull in any data,
#             but it uses the template index.html to render the home page
#     4 - Writing a Simple Template
#         A template sets up the structure for a page
#         It’s a mix of html and template code, which is like Python but not as powerful
#         Make a folder called templates inside the app folder
#         Inside the templates folder make another folder with the same name as the app
#         This is where the template files should be saved
#     5 - Template Inheritance            
#         Many elements of a web page are repeated on every page in the site,
#             or every page in a section of the site.
#         By writing one parent template for the site, and one for each section,
#             you can easily modify the look and feel of your entire site
#     6 - The Parent and Child Templates
#         The parent template defines the elements common to a set of pages, and defines blocks that will be filled by individual pages
#         The child template uses the {% extends 'base.html' %} template tag to pull in the structure of the parent template. 
#             It then defines the content for any blocks defined in the parent template
#             {% block content %} Child Content Here {% endblock content %}


# Building a Page with Data

#     Most pages in a project need to present data that’s specific to the current user

#     1 - URL Parameters
#         A URL often needs to accept a parameter telling it which data to access from the DB
#         Below URL pattern looks for the ID of a specific topic and stores it in the parameter topic_id
#         url(r'^topics/(?P<topic_id>\d+)/$',views.topic, name='topic')
#     2 - Using data in a view
#         The view uses a parameter from the URL to pull the correct data from the database
#         In this below example, the view is sending a context dictionary to the template,
#             containing data that should be displayed on the page



        
    

# Additional Info

# WSGI
#     - Web Server Gateway Interface
#     - Provides a hook for Web Servers such as Apache or EngineX
#     - WSGI is developed for 'calling convention' for web servers
#         to forward requests to web applications or frameworks written in the Python programming language
#     - WSGI was thus created as an implementation-agnostic interface
#         between web servers and web applications or frameworks to promote common ground for portable web application development



