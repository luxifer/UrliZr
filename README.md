[![Build Status](https://secure.travis-ci.org/luxifer/UrliZr.png)](http://travis-ci.org/luxifer/UrliZr)

Installation
============

Settings.py
-----------

First of all copy the `settings.py` file to `local_settings.py`
Don't forget to fill database acces in this file
The you can start the dev server by launching:

    $ python manage.py runserver

API
---

This URL shortener also provide a useful API to integrate in your website
You can retrieve shortened URL in raw, json or xml format just via this url:

    http://<your host>/api/translate/<method>

You just have to pass POST parameters with url containing the url you want to shortened
