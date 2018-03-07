#!/usr/bin/env python
import time
import signal
import sys
import math

class TimeOutError(Exception):
    pass

def timeout(signum, frame, time):
    raise TimeOutError("Timed out after %d seconds" % time)

def run_with_timeout(code, time, globals=None):
    # Set the signal handler and a ``time``-second alarm
    signal.signal(signal.SIGALRM, lambda s, f: timeout(s, f, time))
    if sys.version_info > (2, 5):
        signal.setitimer(signal.ITIMER_REAL, time)
    else:
        # The above only exists in Python 2.6+
        # Otherwise, we have to use this, which only supports integer arguments
        # Use math.ceil to round a float up.
        time = int(math.ceil(time))
        signal.alarm(time)
    r = eval(code, globals)
    signal.alarm(0)          # Disable the alarm
    return r

def pudb_stringifier(obj):
    try:
        return run_with_timeout("type(obj).__name__ + ': ' + str(obj)", 0.5, {'obj':obj})
    except TimeOutError:
        return (type(obj), "(str too slow to compute)")

