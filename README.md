# Python Environment setup
Run:
- `python3 -m venv venv`

This creates are virtual environment.

Run:
- `source /venv/bin/activate`

This activates on the virtual enviroment.

# Django setup

Run:

- `pip install django`

This installs Django module

Run:
- `django-admin startproject django_project`

This creates our Django project. In Django projects contain apps. 

Run:
- `cd django_project`

Inside here we have lots of premade files for us. Manage.py is the one that we will be using most often to pair with commands in the terminal.

Change this file:
- manage.py to use the correct version of python. I changed mine to
    `#!/usr/bin/env `
    
Run:
- `python manage.py startapp blog`

This creates an app for our project.





# Django project files

- urls.py contains our URL routes. There are two types of urls.py: one for the app your created (in this case blog) and for the project. The project one has to import views.py to add new views. The project has to include our app urls.py to map routes.   
- settings.py contains our settings. has lots of good documentation in comments. we will be editing this a lot.
- wsgi.py is used to facilitate how the our project and web server communicate


# Django app files
Django is setup so that a project contains apps. After we create our app we have generated files for these apps.

- views.py facilitates how we view webpages on our site


# Useful Django commands

- `django-admin`

This shows the core django-admin commmands avaiable.

- `python manage.py runserver`

This runs the server
