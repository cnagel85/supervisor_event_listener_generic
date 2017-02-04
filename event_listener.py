
import sys
import inspect
from supervisor import childutils

# EventListener is a genereic event listener for supervisord that allows custom
# handler functions to be registered for handling specified events


class EventListener:
    def __init__(self, defaultHandler=None):
        self.events_map = {}
        self.set_default_handler(defaultHandler)

    def validate_handler(self, handler=None):
        if handler:
            args, _, _, _ = inspect.getargspec(handler)
            if len(args) != 2:
                raise EventListenerError("handlers must have exactly 2 arguments")
            return handler
        else:
            return None

    def set_default_handler(self, handler):
        self.defaultHandler = self.validate_handler(handler)

    def register_event_handler(self, eventname, handler):
        self.events_map[eventname] = self.validate_handler(handler)

    def handle_event(self, headers, payload):
        eventName = headers['eventname']
        handler = self.defaultHandler

        if eventName in self.events_map.keys():
            handler = self.events_map[eventName](headers, payload)

        if handler:
            try:
                handler(headers, payload)
            except TypeError:
                print ""

    def listen(self):
        while True:
            headers, payload = childutils.listener.wait(sys.stdin, sys.stdout)

            self.handle_event(headers, payload)

            childutils.listener.ok(sys.stdout)


class EventListenerError(Exception):
    def __init__(self, message):
        self.message = message
