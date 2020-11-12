# ontrack_project
HCI Project

Instructions to run:

python manage.py migrate --run-syncdb
python population_scipt.py
python manage.py runserver

# HCI Project - Remove all this before final upload
1. Clone git file (All other repos deleted)
* git clone https://github.com/mnolan99/HCI_Project.git

2. open terminal, cd into folder and enter all commands:
* pip install bcrypt
* pip install certifi
* pip install cffi
* pip install Django
* pip install django-cors-headers
* pip install olefile
* pip install Pillow
* pip install pycparser
* pip install pytz
* pip install selenium
* pip install six
* pip install urllib3
* pip install wincertstore

3. Run by entering into terminal:
* python manage.py runserver

4. When adding a new page:
* Create html doc using another template (inside template folder) as a template
* Add a new urlpattern in ontrack_app -> urls.py
* Add a new function in views 
  * e.g. def updates(request): 
  return render(request, 'ontrack_app/updates.html')
* when referencing in another html file, use: 
" <a class="nav-link" href="{% url 'updates'%}">COVID-19 Updates</a> "

5. Issues
* Login/register doesn't work
* Book an appointment button and appointments top right button links to updates page
