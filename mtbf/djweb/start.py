#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
import time
import os
now = time.strftime("%Y%m%d_%H%M" , time.localtime())
os.system('wget http://localhost:8000/mtbf')
locat_path = os.popen('pwd').read()
source = locat_path.rsplit()[0] + "/mtbf"
target = locat_path.rsplit()[0] + "/htmlFolder/" + now + ".html"
shutil.move(source, target)
