# -*- coding: iso-8859-15 -*-

import os
import sys
import tornado
import tornadis
import tornado.web

class RedisConsumer(object):
    def __init__(self, _host="localhost", _port=6379, channel="duckit"):
        self.sockets = {}
        self.channel = channel
        self.pipeline = tornadis.Pipeline()
        self.client = tornadis.PubSubClient(host=_host, port=_port, autoconnect=True)

    @tornado.gen.coroutine
    def add_listener(self, _id, sock):
        self.sockets[_id] = sock

    @tornado.gen.coroutine
    def remove_listener(self, _id):
        del self.sockets[_id]

    @tornado.gen.coroutine
    def subscribe(self):
        yield self.client.pubsub_subscribe(self.channel)

    @tornado.gen.coroutine
    def consume(self):
        print "Subscribing to channel..."
        result = yield self.subscribe()
        print "Now consuming..."
        while True:
            result = yield self.client.pubsub_pop_message()
            if isinstance(result, tornadis.TornadisException):
                # For specific reasons, tornadis nearly never raises any exception
                # they are returned as result
                print "got exception: %s" % result
            else:
                # result is already a python object (a string in this simple example)
                print "Result: %s" % result
                for _id in self.sockets:
                    self.sockets[_id].notify(result)
                # self.pipeline.stack_call("PUBLISH", self.channel, "bar")
                # results = yield self.client.call(self.pipeline)
            



