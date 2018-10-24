# -*- encoding: utf-8 -*-

import re
import sys
import time
import logging
import unicodedata

_logger = logging.getLogger(__name__)

#----------------------------------------------------------
# Functions
#----------------------------------------------------------

def slugify(value):
    value = str(unicodedata.normalize('NFKD', value))
    if sys.version_info < (3,):
        value = str(value.encode('ascii', 'ignore'))
    value = str(re.sub('[^\w\s-]', '', value).strip().lower())
    value = str(re.sub('[-\s]+', '-', value))
    return value

#----------------------------------------------------------
# Decorators
#----------------------------------------------------------

def timeout(func, delay=30):
    def wrapper(*args, **kwargs):
        if args[0]._name in wrapper.timeouts:
            timeout = wrapper.timeouts[args[0]._name]
            if time.time() > timeout + delay:
                wrapper.timeouts[args[0]._name] = time.time()
                return func(*args, **kwargs)
        else:
            wrapper.timeouts[args[0]._name] = time.time()
            return func(*args, **kwargs)
    wrapper.timeouts = {}
    return wrapper