# -*- coding: iso-8859-15 -*-

import os
import sys
import tornado.web
import tornado.escape


class HookHandler(tornado.web.RequestHandler):
    def initialize(self, some_attribute=None):
        self.some_attribute = some_attribute

    @tornado.gen.coroutine
    def get(self):
        self.write("Github Webhook server is running")

    @tornado.gen.coroutine
    def post(self):
        print self.request.body_arguments