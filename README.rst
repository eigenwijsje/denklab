==========================
denklab.org Django project
==========================

This is the complete source code of the Django_ application that powers
http://denklab.org.

Applications
============

The project consists of three applications:

- ``articles``: simple article publishing.
- ``presentations``: simple presentation and additional resources publishing.
- ``projects``: simple project information including release and document
  management.

Requirements
============

This code requires `Django 1.0`_, Markdown_ and the contact_form_ application.
Blueprint_, the CSS framework is also used.

Settings
========

The ``settings.py`` file is not provided but you only need to add
``django.contrib.flatpages.middleware.FlatpageFallbackMiddleware`` to
``MIDDLEWARE_CLASSES` and `django.contrib.flatpages`` to ``INSTALLED_APPS`` if you
want to use the ``flatpages`` contrib application (the corresponding template
is already in place).  

If you want to use the ``contact_form`` application you should install it
according to the `package's documentation`_, the
corresponding templates are also already provided.

You should also set ``MEDIA_ROOT`` and ``MEDIA_URL`` correctly.

Templates
=========

The full set of templates is provided, including the ones required by the
``flatpages`` contrib application and the ``contact_form`` application.  Only
site-specific code like DISQUS_ support has been removed.

Todo
====

- Integrate Tumblr_ and Twitter_ into the homepage.
- Integrate wmd_, The Wysiwym Markdown Editor, into the admin interface.
- Alternatively use Slideshare_'s API to upload presentations.

.. _Blueprint: http://www.blueprintcss.org/
.. _contact_form: http://code.google.com/p/django-contact-form/
.. _`package's documentation`: http://code.google.com/p/django-contact-form/source/browse/trunk/INSTALL.txt
.. _DISQUS: http://disqus.com/
.. _Django: http://www.djangoproject.com/
.. _`Django 1.0`: http://www.djangoproject.com/download/
.. _Markdown: http://pypi.python.org/pypi/Markdown
.. _Slideshare: http://slideshare.net/
.. _Tumblr: http://tumblr.com/
.. _Twitter: http://twitter.com/
.. _wmd: http://wmd-editor.com/
