#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import time
import os
os.system('python3 manage.py runserver')
now = time.strftime("%Y%m%d_%H%M" , time.localtime())
os.system('wget http://localhost:8000/home' + now + ".html")
source = "/home/pc7/pydjango/djweb4/home" + now + ".html"
target = "/home/pc7/pydjango/djweb4/htmlFolder/" + now + ".html"
shutil.move(source , target)

