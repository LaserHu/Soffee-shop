# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Coffees(Resource):

    def get(self):

        return {}, 200, None

    def post(self):
        print(g.args)

        return {}, 200, None