"""
This file contains makes an AWS API call to list ECS clusters N_CALLS times. If
run with an argument, the calls will be made using eventlet monkey-patching.
Otherwise, calls will be made without any greening. Test case and timed results
will be printed to stdout. 
"""
import sys

if use_eventlet := len(sys.argv) > 1:
    import eventlet

    eventlet.monkey_patch()

    pool = eventlet.greenpool.GreenPool()

import time
from contextlib import contextmanager

N_CALLS = 100


@contextmanager
def timeblock():
    label = "with evenlet" if use_eventlet else "without eventlet"
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{N_CALLS} AWS operations {label} : {end-start} seconds")


if __name__ == "__main__":
    with timeblock():
        from eventlet_eval.aws import list_ecs_clusters

        for _ in range(N_CALLS):
            if use_eventlet:
                pool.spawn(list_ecs_clusters, "us-east-1")
            else:
                list_ecs_clusters("us-east-1")

        if use_eventlet:
            pool.waitall()
