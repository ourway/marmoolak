
marmoolak
=========

.. figure:: https://raw.githubusercontent.com/ourway/marmoolak/master/logo.png
   :alt: alt logo


.. image:: https://badge.fury.io/py/marmoolak.svg
    :target: https://badge.fury.io/py/marmoolak

.. image:: https://img.shields.io/pypi/dm/marmoolak.svg
    :target: https://pypi.python.org/pypi/marmoolak




.. image:: https://api.travis-ci.org/ourway/marmoolak.svg
    :target: https://travis-ci.org/ourway/marmoolak

.. image:: https://codecov.io/github/ourway/marmoolak/coverage.svg?branch=master
    :target: https://codecov.io/github/ourway/marmoolak?branch=master


install
-------

::

    pip install marmoolak

Usage
-----

::

    import marmoolak
    marmoolak.REDIS_HOST = '192.168.99.100'
    marmoolak.REDIS_PORT = 6379
    machine = marmoolak.Machine

    def onpanic(e):
        print('panic! ' + e.msg)
    def oncalm(e):
        print('thanks to ' + e.msg + ' done by ' + e.args[0])
    def ongreen(e):
        print('green')
    def onyellow(e):
        print('yellow')
    def onred(e):
        print('red')


    fsm = machine('myname', 'version1' , {'initial': 'green',
                 'events': [
                     {'name': 'warn', 'src': 'green', 'dst': 'yellow'},
                     {'name': 'panic', 'src': 'yellow', 'dst': 'red'},
                     {'name': 'panic', 'src': 'green', 'dst': 'red'},
                     {'name': 'calm', 'src': 'red', 'dst': 'yellow'},
                     {'name': 'clear', 'src': 'yellow', 'dst': 'green'}],
                 'callbacks': {
                     'onpanic': onpanic,
                     'oncalm': oncalm,
                     'ongreen': ongreen,
                     'onyellow': onyellow,
                     'onred': onred }})



    fsm.panic(msg='killer bees', url="http://appido.ir/appido/api/getBooks.json")
    fsm.calm('bob', msg='sedatives in the honey pots')



credits
-------

I used fysom and redis for achiving this functionality. So most of the
credit goes to redis and fysom developers.

Contact me
----------

Feel free to drop me a mail at rodmena@me.com
