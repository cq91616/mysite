#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Terrence Chen
# datetime:2018/10/24 13:26
# software: PyCharm


#!/usr/bin/env python
# coding: utf-8

import os
import sys

# 将系统的编码设置为UTF8
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")#mysite替换为自己的项目名

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

