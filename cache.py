#cache.py

import datetime

MAX_CACHE_SIZE = 100
_cache = {}

##################################################


def init():
    global _cache
    _cache = {}


def set(key, value):
    global _cache
    if key not in _cache and len(_cache) >= MAX_CACHE_SIZE:
        _remove_oldest_entry()
    _cache[key] = [datetime.datetime.now(), value]


def get(key):
    global _cache
    if key in _cache:
        _cache[key][0] = datetime.datetime.now()
        return _cache[key][1]
    else:
        return None


def size():
    global _cache
    return len(_cache)

###################################################

# Private functions:

def _remove_oldest_entry():
    global _cache
    oldest = None
    for key in _cache.keys():
        if oldest == None:
            oldest = key

        if oldest != None:
            del _cache[oldest]
