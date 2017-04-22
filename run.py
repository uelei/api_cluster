# -*- coding: utf-8 -*-
from back.factory import create_app
__author__ = 'wesleywwerneck'

app = create_app("config/local.py")

if __name__ == '__main__':

    # from back.main import *
    app.run()
