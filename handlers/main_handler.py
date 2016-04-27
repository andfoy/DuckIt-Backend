# -*- coding: iso-8859-15 -*-

import os
import sys
import tornado.web
import tornado.escape

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, some_attribute=None):
        self.some_attribute = some_attribute

    @tornado.gen.coroutine
    def get(self):
    	self.render('../static/starter.html')

    @tornado.gen.coroutine
    def post(self):
    	self.status_code(403)