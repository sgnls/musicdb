musicdb
=======

.. image:: https://api.travis-ci.org/lamby/musicdb.svg?branch=master
  :target: https://travis-ci.org/musicdb/musicdb

.. image:: https://coveralls.io/repos/lamby/musicdb/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/lamby/musicdb?branch=master

.. image:: https://requires.io/github/musicdb/musicdb/requirements.svg?branch=master
  :target: https://requires.io/github/musicdb/musicdb/requirements/?branch=master

This is my personal media library which I wrote after being frustrated with
other solutions which use pre-1970s database technology.

The feature-set is mostly geared towards accurately storing western classical
music circa 1500 to the present day. It also supports albums ("non-classical")
too with correct support for multiple CDs.

It is entirely web-based and generates XSPF files pointing to the actual files.

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
