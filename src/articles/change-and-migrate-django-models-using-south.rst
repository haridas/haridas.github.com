Change and Migrate Django Models using South
############################################
:date: 2011-06-17 10:41
:category: blog
:tags: python,django,south

.. image:: /images/south.png

South is very handy django application to manage the django models. If
we are developing web projects using django we need to change the Django
model several times , In normal case we have to do these changes
manually by editing both django model and backend database
appropriately. This is very frustrating if we have to do it several
times.

The South application makes it very easy to handle the model changes
and fill the initial data's into the database tables. To setup the South
application along with your django project, you need to do very simple
changes to the settings.py file of your django project. To make it
simple you have to do this step before adding any of your django apps to
the project.

First of all install the south application to your system.

.. code-block:: console

   #easy_install south

then you have to add your south app to django settings.py file under
 

INSTALLED_APPS veriable, ie;

.. code-block:: python

 INSTALLED_APPS = (
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.sites',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 # Uncomment the next line to enable the admin:
 'django.contrib.admin',
 # Uncomment the next line to enable admin documentation:
 # 'django.contrib.admindocs',
 'south', # <---HERE
 )

Now we added the south app to our django project, the commands
associated with this app is comes under the manage.py.

Next step is to sync all models to the backend database, for that you
have to use the usual method , ie;

.. code-block:: console

 Migrate all tables to backend database,
 it includes our south apps tables.

 $python manage.py syncdb

That's it !. we are now ready to use south app for our apps model
management.

Currently we added tables of default django apps and south app to
backend. Now we are ready to add our applications to django project.
After adding new django application to the sttings.py INSTALLED_APPS
variable, we need to migrate it's models using south management
commands,

.. code-block:: console

 Initially you have to add new app under south , for that,
 python manage.py schemamigration your_app --initial
 This will setup your app under south, need to run only once,
 Then migrate models to backend database,

 $python manage.py migrate your_app



After the initial addition of your django app under south, to migrate
the future model changes under the same app, you have to do the bellow
steps,

.. code-block:: console

 After any changes to your model,
 First detect those changes ,

 $python manage.py schemamigration your_app --auto

 Then Migrate to backend,

 $python manage.py migrate your_app

So using south app you are now manged model changes without touching
backend database. In this manner we can manage all django applications
under your project.

Try this out ! and save your time.
