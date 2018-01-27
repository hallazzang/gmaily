gmaily
======

Pythonic Gmail client (WIP)

Features
--------

- [x] Clean API
- [x] No other dependencies than standard libraries
- [-] Supports all of the ``SEARCH`` criteria
- [-] Supports access to all of the ``HEADER`` fields via attributes
- [ ] Lazy loading for contents

Example
-------

.. code:: python

    import sys
    import getpass
    import datetime

    from gmaily import Gmaily

    g = Gmaily()

    user_email = input('Email: ')
    user_pw = getpass.getpass()

    if not g.login(user_email, user_pw):
        print('Cannot login')
        sys.exit(1)

    msgs = g.inbox().after(datetime.date.today() - datetime.timedelta(weeks=2))
    for msg in msgs.all():
        print('\n' + (' Mail UID: %d ' % msg.uid).center(80, '=') + '\n')
        print('Subject:', msg.subject)
        print('From:', msg.sender)
        print('Date:', msg.date)
        print('Attachments:', msg.attachments)

        print('-' * 10)
        print(msg.text)

    g.logout()

Installation
------------

Currently it requires Python 3.

.. code:: bash

    $ pip install gmaily

License
-------

MIT
