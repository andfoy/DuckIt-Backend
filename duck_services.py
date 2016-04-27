#!/usr/bin/env python

import os
import sys
import logging
import tornado.web
import coloredlogs
import tornado.ioloop
from middleware import redis_publisher
from handlers.backlayer import services_handler

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)
coloredlogs.install(level='info')

clr = 'clear'
if os.name == 'nt':
   clr = 'cls'

def main():
  application = tornado.web.Application([(r"/duckit", services_handler.ServicesHandler)],
              debug=True, serve_traceback=True, autoreload=True)
  print "Server is now at: 127.0.0.1:8002"
  print "Press Ctrl-C to Stop"
  ioloop = tornado.ioloop.IOLoop.instance()
  redis = redis_publisher.RedisPublisher()
  application.redis = redis
  application.listen(8002)
  try:
    ioloop.start()
  except KeyboardInterrupt:
    pass
  finally:
    print "Closing server...\n"
    tornado.ioloop.IOLoop.instance().stop()

if __name__ == '__main__':
   os.system(clr)
   main()

