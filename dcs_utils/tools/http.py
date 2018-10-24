# -*- encoding: utf-8 -*-

import urllib
import logging

import requests
import werkzeug

from odoo.http import request
from odoo.tools import config

_logger = logging.getLogger(__name__)

def get_route(url):
    url_parts = url.split('?')
    path = url_parts[0]
    query_string = url_parts[1] if len(url_parts) > 1 else None
    router = request.httprequest.app.get_db_router(request.db).bind('')
    match = router.match(path, query_args=query_string)
    method = router.match(path, query_args=query_string)[0]
    params = dict(urllib.parse.parse_qsl(query_string))
    if len(match) > 1:
        params.update(match[1])
    return method, params, path

def make_error_response(status, message):
    exception = werkzeug.exceptions.HTTPException()
    exception.code = status
    exception.description = message
    return exception

def get_response(url):
    if not bool(urllib.parse.urlparse(url).netloc):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        method, params, path = get_route(url)
        params.update({'csrf_token': request.csrf_token()})
        session = requests.Session()
        session.cookies['session_id'] = request.session.sid
        try:
            response = session.post("%s%s" % (base_url, path), params)
            return response.status_code, response.headers, response.content
        except requests.exceptions.RequestException as exception:
            return exception.response.status_code, exception.response.headers, exception.response.reason
    else:
        try:
            response = requests.get(url)
            return response.status_code, response.headers, response.content
        except requests.exceptions.RequestException as exception:
            return exception.response.status_code, exception.response.headers, exception.response.reason
    
