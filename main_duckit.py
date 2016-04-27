#!/usr/bin/env python

import os
import sys
import logging
import tornado.web
import coloredlogs
import redis_consumer
import tornado.ioloop
from handlers import main_handler
from handlers import websocket_handler

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)
coloredlogs.install(level='info')

clr = 'clear'
if os.name == 'nt':
   clr = 'cls'

def main():
  settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}
  application = tornado.web.Application([(r"/", main_handler.MainHandler),
                (r'/feed', websocket_handler.WebSocketHandler)],
              debug=True, serve_traceback=True, autoreload=True, **settings)
  print "Server is now at: 127.0.0.1:8001"
  ioloop = tornado.ioloop.IOLoop.instance()
  redis = redis_consumer.RedisConsumer()
  application.redis = redis
  application.redis.consume()
  application.listen(8001)
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

