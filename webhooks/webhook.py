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
        print self.request.headers['X-GitHub-Event']
        print self.request.headers['Random']
        data = tornado.escape.json_decode(self.request.body)
        print data.keys()