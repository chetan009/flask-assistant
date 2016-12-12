from . import logger
from flask import json, Response, make_response
from xml.etree import ElementTree


class _Response(object):
    """docstring for _Response"""
    def __init__(self, speech):
        
        self._json_default = None
        self._response = {
            'speech': speech,
            'displayText': '',
            'data': {},
            'contextOut': [],
            'source': 'webhook'

        }

    def display_text(self, text):
        self._response['displayText'] = text
        return self

    def add_context(self, context_dict):
        self._response['contextOut'] = context_dict
        return self

    def add_source(self, source):
        self._response['source'] = source
        return self



    def render_response(self):
        _dbgdump(self._response)
        resp = json.dumps(self._response, indent=4)
        resp = make_response(resp)
        resp.headers['Content-Type'] = 'application/json'
        return resp


def _dbgdump(obj, indent=2, default=None, cls=None):
    msg = json.dumps(obj, indent=indent, default=default, cls=cls)
    logger.debug(msg)
