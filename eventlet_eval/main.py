"""
This file contains makes an AWS API call to list ECS clusters 10 times. If run
with an argument, the calls will be made using eventlet patching. Otherwise,
calls will be made without any greening. Test case and timed results will be
printed to stdout. 
"""

import sys

use_eventlet = len(sys.argv) > 1
if use_eventlet:
    import eventlet

    eventlet.monkey_patch()

import time
from contextlib import contextmanager

import boto3
from botocore.config import Config

N_CALLS = 100


@contextmanager
def timeblock(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{N_CALLS} AWS operations {label} : {end-start} seconds")


def ecs_region(region_name):
    cfg = Config(
        region_name=region_name,
    )
    ecs = boto3.client("ecs", config=cfg)
    try:
        result = ecs.list_clusters(maxResults=100)
    except Exception as e:
        result = {"exception": e}
        n_clusters = 0
    else:
        n_clusters = len(result["clusterArns"])

    return f"{region_name}\t{result}\t{n_clusters}"


label = "with evenlet" if use_eventlet else "without eventlet"

with timeblock(label):
    for _ in range(N_CALLS):
        ecs_region("us-east-1")
