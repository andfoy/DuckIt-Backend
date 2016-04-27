# -*- coding: iso-8859-15 -*-

import os
import sys
import tornado.web
import tornado.escape

class ServicesHandler(tornado.web.RequestHandler):
    def initialize(self, some_attribute=None):
        self.some_attribute = some_attribute

    @tornado.gen.coroutine
    def get(self):
    	self.status_code(403)

    @tornado.gen.coroutine
    def post(self):
    	print self.request.body
    	self.application.redis.publish_channel(self.request.body)