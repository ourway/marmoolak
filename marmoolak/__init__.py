

__author__ = 'Farsheed Ashouri'


import hashlib
import redis
import os

REDIS_HOST = None
REDIS_PORT = None

from fysom import Fysom as _Fysom


class Machine(_Fysom):

    def __init__(self, name, version, *args, **kw):
        """ Usage: Machine("name", 1.0, *args, **kw)"""
        ''' Redis setup'''
        redis_host = REDIS_HOST or os.getenv('REDIS_HOST') or 'localhost'
        _redis_port = REDIS_PORT or os.getenv('REDIS_PORT') or '6379'
        redis_port = int(_redis_port)
        self.r = redis.StrictRedis(host=redis_host, port=redis_port)


        self.rhname = 'appido_core_fsm_{n}_{v}'.format(n=name, v=version)
        history = self.r.get(self.rhname)
        if history:
            args[0]['initial'] = history
        self.name = name
        self.version = version
        super(Machine, self).__init__(*args, **kw)




    def _after_event(self, e):
        '''
            Checks to see if the callback is registered for, after this event is completed.
        '''
        ''' my patch, serialize to redis '''
        self.r.set(self.rhname, self.current)
        for fnname in ['onafter' + e.event, 'on' + e.event]:
            if hasattr(self, fnname):
                return getattr(self, fnname)(e)

    def __hash__(self):
        return hashlib.md5(self.name).hexdigest()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)



