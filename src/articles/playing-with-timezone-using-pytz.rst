playing with timezone using pytz
################################
:date: 2011-05-11 04:15
:category: programming
:tags: python,pytz,timezone

World Timezone Image from www.physicalgeography.net

.. image:: /images/world_time2-300x172.gif
    :width: 100%

When we develop web applications some times we need multiple timezone
support. If we don’t have any previous experience then it might be a
tough and confusing job. Here I will help you to get some basics of
Timezone conversion.

I have been used timezone with django application, but the concept is
same for all languages.So here I will explain things using python
timezone module "pytz". You have to install this module first into your
system by using "easy_install"

Install python timezone module.

.. code-block:: console

   #easy_install pytz 



This python module support all major timezones and it helps to convert
date and time in one timezone to any other timezones.You can use the
human readable tiemzone names in pytz module to represent the local
timezones.( like Asia/Kolkata, Europe/Paris, EST etc. ).

When we deal with multiple timezone in our application, we might have
backend database where we store these date and time informations. Most
databases are support UTC as it's the common timezone format. And it's
better to keep a unique timezone information when saving the date and
time in database and database engines not going to support all timezone
formats directly. So we need to stick with commonly used **UTC/GMT**
(Coordinated Universal Time) timezone format , it also helps to remove
the daylight saving issues.

Here is the strategies used in web applications with multiple timezone
support :-

#. Save Date and Time information’s in database as UTC format.
#. Convert the UTC time to corresponding local timezones, based on the
   user request and location.
#. We take local timezone information from browser or user select a
   timezone form the list of timezones that supported by our
   application. We can collect this information easily with the help of
   Javascript.

Bellow I'm explaining some real scenarios where we need to change time
zone information's from UTC to local and vice versa,

**1. Saving Date and Time in Database :-**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We always save date and time information in database as UTC standard.
In django/Rails or other Framworks we have an option to set Projects
default tiemzone as UTC. So in our database the time and date are always
in UTC. If above methods are not working for your application you
manually need to convert the local system time into UTC format and then
save it. Below code sample explain things more clearly,

.. code-block:: pycon
   
   haridas@haridas-debian:~$ python
   Python 2.6.6 (r266:84292, Dec 27 2010, 00:02:40)
   [GCC 4.4.5] on linux2
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   >>> import pytz
   >>> import datetime
   >>> local_system = datetime.datetime.now() #Get local system time and
       date.
   >>> local_system
   datetime.datetime(2011, 5, 7, 9, 42, 23, 751976)
   >>>
   >>> local_system_utc = datetime.datetime.utcnow() # utcnow() function
        give the UTC time of current local time.
   >>> local_system_utc # But this date tupple doesn't have the timezone
         information.
         datetime.datetime(2011, 5, 7, 5, 42, 49, 253618) #We call it as Naive
        representation(Date object without Timezone information.)
   >>>
   >>> local_system_utc.tzinfo #This output None value or nothing.
   >>>
   >>>
   >>> local_system_utc = pytz.utc.localize(local_system_utc) #Adding
        timezone information to "local_system_utc"

   >>>
   >>> local_system_utc
        datetime.datetime(2011, 5, 7, 5, 42, 49, 253618, tzinfo=<UTC>) #you can
        see the tzinfo variable included with the datetime tuple.
        #But when saving UTC time inside DB you can use naive representation of
        datetime object in UTC.
        #You can do the tzinfo addition when retrieving the time from DB.

By this way we can save time and date in Database even-though users are
from different timezone. We need to consider them only when retrieving
the time object from database, ie; we need to convert our UTC time to
user specific timezone. So this conversion is only for view purpose.

**2. Converstion from UTC to localtime**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to convert UTC times to corresponding user timezone, follow the
bellow method,

.. code-block:: pycon

 >>> import pytz
 >>> import datetime
 >>>
 >>> now_utc = datetime.datetime.utcnow() #Our UTC naive time from DB,
    for the time being here I'm taking it as current system UTC time..
 >>> now_utc
     datetime.datetime(2011, 5, 9, 6, 36, 39, 883479) # UTC time in Naive
    form.
 >>>
 >>> local_tz = pytz.timezone('Europe/Paris') #Our Local timezone, to
    which we want to convert the UTC time.
 >>>
 >>> now_utc = pytz.utc.localize(now_utc) #Add Timezone information to
    UTC time.
 >>>
 >>> now_utc
 datetime.datetime(2011, 5, 9, 6, 36, 39, 883479, tzinfo=<UTC>) # The
    full datetime tuple
 >>>
 >>> local_time = now_utc.astimezone(local\_tz) # Convert to local
    time.
 >>>
 >>> local_time #Current local time in Paris
 datetime.datetime(2011, 5, 9, 8, 36, 39, 883479, tzinfo=<DstTzInfo
    'Europe/Paris' CEST+2:00:00 DST>)
 >>>

**3. Manage Browser Local Time at Server**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rather than just conversion of UTC time, some times we need to fetch
records from the Database in between particular interval of local time
time, for eg; From 07:00 Morning to 22:30 Evening of local time. Here
our data is in UTC format, so we need to get the corresponding UTC time
of these local time interval and then search the DB, you can follow
bellow method,

#. From browser you will get time in epoch format (A unique number to
   represent a particular time) or in string format ie; Y-M-D-H-M-S
#. Convert this epoch time to python UTC time.
#. Then search the Database.

You can reconstruct the javascrpt string format of the date in to
python date object by,

.. code-block:: pycon

 >>> import datetime
 >>> import pytz
 >>>
 >>>
    datetime.datetime(year=2011,month=6,day=7,hour=10,minute=26,second=45)
     datetime.datetime(2011, 6, 7, 10, 26, 45)
 >>> local_date =
    datetime.datetime(year=2011,month=6,day=7,hour=10,minute=26,second=45)
 >>>
 >>>
 #From DB we will get the corresponding users timezone information , for
    eg; we can take 'America/Chicago' as our local timezone.
 >>> timezone = pytz.timezone('America/Chicago')
 >>> local_std_date = timezone.localize(local\_date,is\_dst=True)
 >>>
 >>> local_std_date
 datetime.datetime(2011, 6, 7, 10, 26, 45, tzinfo=<DstTzInfo
    'America/Chicago' CDT-1 day, 19:00:00 DST>)
 >>>
 >>>
 #Now you have standard localtime and it can be easily converted to the
    UTC and then do the Database search and other things.
 >>> local_utc = local_std\_date.astimezone(pytz.utc)
 >>> local_utc
 datetime.datetime(2011, 6, 7, 15, 26, 45, tzinfo=<UTC>)
 >>>

