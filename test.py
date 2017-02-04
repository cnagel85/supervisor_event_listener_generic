#!/usr/bin/env python

import event_listener


def default_handler(headers, payload):
    print "handled by default"


def valid_handler(headers, payload):
    print "headers: ", headers
    print "payload: ", payload


def invalid_test_handler(headers):
    print "invalid handler"


class Test:
    def __init__(self, name):
        self.name = name
        self.failed = False

    def run(self):
        print "\nRunning test [%s]..." % self.name

    def fail(self):
        self.failed = True

    def passed(self):
        self.failed = False

    def result(self):
        result = 'passed'
        if self.failed:
            result = "failed"
        print "test [%s] %s" % (self.name, result)


if __name__ == '__main__':
    listener = event_listener.EventListener()

    # no default handler test
    test = Test("blank default handler")
    try:
        test.run()
        print "handling event..."
        listener.handle_event({'eventname': 'default'}, "default test")

    except event_listener.EventListenerError:
        print "failed"
        test.fail()
    test.result()

    # default handler test
    test = Test("default handler")
    try:
        test.run()
        print "creating new handler with default handler..."
        defaultListen = event_listener.EventListener(default_handler)

        print "handling event..."
        defaultListen.handle_event({'eventname': 'default'}, "default test")

    except event_listener.EventListenerError:
        print "failed"
        test.fail()
    test.result()

    # valid handler test
    test = Test("valid handler")
    try:
        test.run()
        print "registering..."
        listener.register_event_handler('valid', valid_handler)

        print "handling event..."
        listener.handle_event({'eventname': 'valid'}, "valid test")

    except event_listener.EventListenerError:
        print "failed"
        test.fail()
    test.result()
