# -*- encoding: utf-8 -*-

import logging

from odoo import api

_logger = logging.getLogger(__name__)

def monkey_patch(cls):
    def decorate(func):
        name = func.__name__
        func.super = getattr(cls, name, None)
        setattr(cls, name, func)
        return func
    return decorate

def monkey_patch_model(cls):
    def decorate(func):
        name = func.__name__
        super = getattr(cls, name, None)
        func.super = super
        wrapped = api.guess(api.propagate(name, func))
        wrapped.super = super
        setattr(cls, name, wrapped)
        return func
    return decorate
