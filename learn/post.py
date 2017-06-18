#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 19:05:16
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib
import urllib2

values = {"username":"test@qq.com", "password":"pw"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
