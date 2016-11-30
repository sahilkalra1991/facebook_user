# facebook_user

Requirements:
1. Python 3.4+
2. Django 1.9+

Setup instructions:
1. Environment Setup:
    1. Create a virtual environment with Python 3.4+ and activate it
        >virtualenv --python=<path to python 3> env

    2. Move to project directory
    3. Execute: pip install -r requirements.txt
2. MySQL: 
    1. Setup a Database name "fb_user" with user "root"
    2. Execute:
        >python manage.py migrate

3. Create a SuperUser:
    >python manage.py createsuperuser
4. Edit your hosts file to point localhost.com to 127.0.0.1
5. Setup Django-Allauth: http://django-allauth.readthedocs.io/en/latest/installation.html#post-installation
6. Open homepage: localhost.com:8000/
