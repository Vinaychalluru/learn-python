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
#         To define the models for your app, modify the models.py created in app's folder
#         The __str__() method tells Django how to represent data Objects based on this model
#     2 - Activating a Model
#         To use a model, the app must be added to the tuple
#         INSTALLED_APPS, which is stored in the project’s settings.py file
#     3 - Migrating the Database
#         The database needs to be modified to store the kind of data that the model represents
#         python .\manage.py makemigrations learning_logs
#     4 - Creating a superuser
#         A superuser is a user account that has access to all aspects of the project
#         python .\manage.py createsuperuser
#     5 - Registering a Model
#         You can register your models with Django’s admin site, 
#         which makes it easier to work with the data in your project
#         To do this, modify the app’s admin.py file
#         View the admin site at http://localhost:8000/admin

# Building a Simple Home Page

#     Users interact with a project through web pages, and a 
#     project’s home page can start out as a simple page with no data
#     A page usually needs a URL, a view, and a template.

#     1 - Mapping a Project's URL
#         The project’s main urls.py file tells Django
#         where to find the urls.py files associated with each app in the project
#     2 - Mapping an App's URL
#         An app’s urls.py file tells Django which view to use for each URL in the app
#         You’ll need to make this file yourself, and save it in the app’s folder.
#     3 - Writing a Simple View
#         A view takes information from a request and sends data to the browser, often through a template
#         View functions are stored in an app’s views.py file
#         This simple view function doesn’t pull in any data,
#             but it uses the template index.html to render the home page



