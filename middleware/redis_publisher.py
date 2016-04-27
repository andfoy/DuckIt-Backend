# -*- coding: iso-8859-15 -*-

import os
import sys
import tornado
import tornadis
import tornado.web

class RedisPublisher(object):
    def __init__(self, _host="localhost", _port=6379):
        self.client = tornadis.Client(host=_host, port=_port, autoconnect=True)

    @tornado.gen.coroutine
    def publish_channel(self, msg, channel="duckit"):
        # Let's make a pipeline object to stack commands inside
        pipeline = tornadis.Pipeline()
        pipeline.stack_call("PUBLISH", channel, msg)

        # At this point, nothing is sent to redis

        # let's (re)connect (autoconnect mode), send the pipeline of requests
        # (atomic mode) and wait all replies without blocking the tornado ioloop.
        results = yield self.client.call(pipeline)

        if isinstance(results, tornadis.TornadisException):
            # For specific reasons, tornadis nearly never raises any exception
            # they are returned as results
            print "got exception: %s" % results
        else:
            # The two replies are in the results array
            print results