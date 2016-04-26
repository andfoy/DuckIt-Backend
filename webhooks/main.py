#!/usr/bin/env python

import os
import sys
import base64
import webhook
import tornado.web
import tornado.ioloop

clr = 'clear'
if os.name == 'nt':
   clr = 'cls'

def main():
  with open('../secret.k', 'rb') as fp:
       lines = fp.readlines()
  line = lines[0]
  secret = base64.b64decode(line)
  repos = {'DuckIt-Backend':'~/DuckIt-Backend/deploy.sh'}
  application = tornado.web.Application([(r"/", webhook.HookHandler)],
              debug=True, serve_traceback=True, autoreload=True)
  print "Server is now at: 127.0.0.1:8000"
  ioloop = tornado.ioloop.IOLoop.instance()
  application.repos = repos
  application.listen(8000)
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

