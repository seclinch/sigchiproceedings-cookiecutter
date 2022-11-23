# -*- coding: utf-8 -*-
from jinja2.ext import Extension


def slug(value):
    return value


class PaperTitleExtension(Extension):
    def __init__(self, environment):
        super(PaperTitleExtension, self).__init__(environment)
        environment.filters['slug'] = slug
