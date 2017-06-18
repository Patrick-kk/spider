#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 19:10:36
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib
import os.path

url = 'http://gw2.alicdn.com/tfscom/tuitui/TB1SuzNJVXXXXajXVXXXXXXXXXX_468x468q75.jpg'


filename = 'image_test'+os.path.splitext(url)[1]
with open(filename, 'wb') as f:
    u = urllib.urlopen(url)
    data = u.read()
    f.write(data)
