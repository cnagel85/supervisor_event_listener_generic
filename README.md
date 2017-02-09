# Generic Supervisord Event Listener

## Description
EventListener is a generic supervisor event listener class that allows you to register handler functions to handle named supervisor events

## Simple Setup

Copy or import event_listener.py into your script

```python
if __name__ == '__main__':
	#Create a new event listener instance
	listener = event_listener.EventListener()

	# Register Handlers
	listener.register_event_handler('event_1', my_handler1)
	listener.register_event_handler('event_2', my_handler2)

	# start listener
	listener.listen()
```

## Handler Functions
Event handler functions need to accept two arguements for the headers and payload dictionaries that are the return values from childutils.listener.wait() from the supervisor library.
Header tokens are listed at [Supervisor Events Documentation](http://supervisord.org/events.html#header-tokens) and the payload is deteremined by the type of event and can be found in the supervisor event types documentation


```python
def handler(headers, payload):
	print "handled"
```
Only one handler can be registered per event

### Example Handler
```python

def handle_process_exited(headers, payload):
    print "handling exited process..."

    ph, pdata = childutils.eventdata(payload + '\n')
    if not int(ph['expected']):
        print "process [%s] with pid [%s] exited unexpectedly" % (
              ph['processname'], ph['pid'])

    print "exited process handled"
```

## References
* [Supervisor Documentation](http://supervisord.org/index.html)
