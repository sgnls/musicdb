musicdb
=======

This is my personal music database which I wrote after being frustrated with
the "media libraries" which use pre-1970s database technology.

The feature-set is mostly geared towards accurately storing western classical
music circa 1500 to the present day. It also supports albums ("non-classical")
too with correct support for multiple CDs.

It is entirely web-based and generates M3U or XSPF files pointing to the actual
files.

Local database setup
--------------------

 #. Create PostgreSQL user with id matching your UNIX username::

    $ sudo -u postgres createuser $(whoami) -SDR

 #. Create a database owned by this user::

    $ sudo -u postgres createdb -E UTF-8 -O $(whoami) musicdb

 #. Check we can connect to this database::

    $ /usr/bin/psql musicdb
    psql (9.1.2)
    Type "help" for help.
    
    musicdb=> \q

Syncing with the live site (lamby only)
---------------------------------------

Sync database::

    $ ./manage.py sync_database
