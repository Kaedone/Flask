#!/home/39896/python/bin/python
# -*- coding: utf-8 -*-
import sys, os

sys.path.insert(0, "/home/39896/Flask")

from flup.server.fcgi import WSGIServer
from myapp import app

if__name__ == '__main__':
    WSGIServer(app).run()
