# marmoolak
Yet another finite state machine with memory


![alt logo](logo.png)

### install ###
```
pip install marmoolak
```

### Usage ###

```
from marmoolak import Machine

def onpanic(e):
    print 'panic! ' + e.msg
def oncalm(e):
    print 'thanks to ' + e.msg + ' done by ' + e.args[0]
def ongreen(e):
    print 'green'
def onyellow(e):
    print 'yellow'
def onred(e):
    print 'red'


fsm = Machine('myname', 'version1' , {'initial': 'green',
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



fsm.panic(msg='killer bees', url="http://appidi.ir/api/getBooks.json")
fsm.calm('bob', msg='sedatives in the honey pots')
```


### credits ###
I used fysom and redis for achiving this functionality. So most of the credit goes to redis and fysom developers.

### Contact me ###

Feel free to drop me a mail at rodmena@me.com
