#!/usr/bin/env python

import event_listener
from supervisor import childutils


def handle_process_exited(headers, payload):
    print "handling exited process..."

    ph, pdata = childutils.eventdata(payload + '\n')
    if not int(ph['expected']):
        print "process [%s] with pid [%s] exited unexpectedly" % (
              ph['processname'], ph['pid'])

    print "exited process handled"


if __name__ == '__main__':
    listener = event_listener.EventListener()
    listener.register_event_handler('PROCESS_STATE_EXITED',
                                    handle_process_exited)
    listener.listen()
