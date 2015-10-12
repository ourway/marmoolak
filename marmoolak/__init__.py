

__author__ = 'Farsheed Ashouri'


import hashlib
import redis
r = redis.StrictRedis()
from fysom import Fysom as _Fysom


class Machine(_Fysom):

    def __init__(self, name, version, *args, **kw):
        self.rhname = 'appido_core_fsm_{n}_{v}'.format(n=name, v=version)
        history = r.get(self.rhname)
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
        r.set(self.rhname, self.current)
        for fnname in ['onafter' + e.event, 'on' + e.event]:
            if hasattr(self, fnname):
                return getattr(self, fnname)(e)

    def __hash__(self):
        return hashlib.md5(self.name).hexdigest()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)



