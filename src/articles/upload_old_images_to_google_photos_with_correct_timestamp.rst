Upload old images into google photos with correct timestamp
###########################################################

:date: 2016-01-08 16:29
:catogory: blog
:tags: sync, photo


After my WD Pasport got corrupted, I had to back all my precious old photos into
another backup location. Google photos was the excellege option as I'm
using Android and uploading the photos to it. And it has multiple features like

1. Duplicate detection while uploading photos.
2. Auto taging, searching.
3. Easily accessible on multiple platforms
4. Order the photos

Keeping all photos in one place and seeing them year / month wise is what I want
to do. Google photos really does this if we enable the photo sync in Android phone.

But when I uploaded old photos ( ie; pre 2011 ) what happens is that, old photos
are got mixed up with new photos that I took in 2015. I renamed the files with
time stamp (eg: IMG_20090911_234433.jpg) thinking that now it will sort it correctly,
but didn't happen.

Google photos have option to change date of one file, but no bulk editing or
editing the album date range. Further googling revealed that
google photos using the `EXIF`_ meta tag `Exif.Photo.DateTimeOriginal` for
ordering the images that we uploaded to it.

.. _`EXIF`: https://en.wikipedia.org/wiki/Exchangeable_image_file_format

Most of the photos that we took has all required EXIF records available,
but the problem comes if you took photos using some old devices or old Phones,
then you are unlucky.  Another problem is even though if you have EXIF tag `Exif.Photo.DateTimeOriginal`
record but your camera datetime is wrong you are still facing this problem.

So how we edit the EXIF meta data so that while uploading google photos will
order it correctly.

Luckily we have set of utilities available to edit EXIF tags in an image.
`exiv2`_ is the one of it.

.. _`exiv2`: http://www.exiv2.org/


It's available on all platforms. Lets install and checkout some samples.

.. code-block:: bash

    $ sudo apt-get install exiv2


How to change single photo's EXIF record using exiv2 tool.

.. code-block:: text

    $ exiv2 -M"add Exif.Photo.DateTimeOriginal 2009:03:05 00:00:00" IMG_20090305_000553.jpg

We are adding Exif header to this photo with correct time that we took this
photo. How we know this date, that's up to you to decide :). The bellow script that
I attached has option to pick the date time from the filename format or from its 
modification time.

To check your photo has all expected Exif records use this command,

.. code-block:: text

    $ exiv2 -pt IMG_200090305_000553.jpg

If you noticed one thing, if we add the `Exif.Photo.DateTimeOriginal`
multiple times, then duplicate entries are being creatd in the EXIF tags.
If you want to remove records from EXIF, you can do it using exiv2 command.

.. code-block:: text

    $ exiv2 -M"del Exif.Photo.DateTimeOriginal 2009:03:05 12:03:35" IMG_20090303_000550.jpg


Now lets automate the process in a script,

On platforms other than Linux, you can find google photos desktop application to
upload old photos. Please try that out if it compatible to your machine.

Here is the scripts that I used to do this,

[gist:id=6905941c73a28492fa43]

Now simply give following commands to update your file's EXIF tag `Exif.Photo.DateTimeOriginal`.

The bellow command will find all the "jpg" files in your current and sub folders
and using the above python script update the Exif tag if it doesn't exist.

.. code-block:: bash

    for file in `find . -iname "*.jpg"`; do python add_exif_record.py -t ftime -f $file; done


