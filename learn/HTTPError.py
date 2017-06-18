#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 20:51:10
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib2

request = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
    print e.reason
else:
    print 'OK'
