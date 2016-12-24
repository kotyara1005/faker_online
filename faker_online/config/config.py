# -*- coding: UTF-8 -*-
DEBUG = True

STATIC_FOLDER = None

try:
    from faker_online.config.local_settings import *
except ImportError:
    pass
