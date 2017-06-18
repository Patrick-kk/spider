#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 20:31:13
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib2

request = urllib2.Request('http://www.xxxgsx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

