# -*- encoding: utf-8 -*-

import os
import io
import base64
import shutil
import urllib
import logging
import tempfile
import mimetypes

from odoo.tools import config
from odoo.tools.mimetypes import guess_mimetype

_logger = logging.getLogger(__name__)

def unique_name(name, names, escape_suffix=False):
    def compute_name(name, suffix, escape_suffix):
        if escape_suffix:
            name, extension = os.path.splitext(name)
            return "%s(%s)%s" % (name, suffix, extension)
        else:
            return "%s(%s)" % (name, suffix)
    if not name in names:
        return name
    else:
        suffix = 1
        name = compute_name(name, suffix, escape_suffix)
        while name in names:
            suffix += 1
            name = compute_name(name, suffix, escape_suffix)
        return name
    
def get_extension(binary, filename, mimetype):
    extension = None
    if not mimetype and not filename:
        mimetype = guess_mimetype(binary, default=False)
    if not mimetype and filename:
        mimetype = mimetypes.guess_type(urllib.request.pathname2url(filename))[0]
    if filename:
        extension = os.path.splitext(filename)[1][1:].strip().lower() 
    if not extension and mimetype and mimetype != 'application/octet-stream':
        extension = mimetypes.guess_extension(mimetype)[1:].strip().lower()
    return extension