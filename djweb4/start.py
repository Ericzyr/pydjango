#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
import time
import os
# os.system('python3 manage.py runserver')
now = time.strftime("%Y%m%d_%H%M" , time.localtime())
os.system('wget http://localhost:8000/home' + now + ".html")
locat_path = os.popen('pwd').read()
source = locat_path.rsplit()[0] + "/home" + now + ".html"
target = locat_path.rsplit()[0] + "/htmlFolder/" + now + ".html"
shutil.move(source, target)

