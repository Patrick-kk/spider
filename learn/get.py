#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 19:28:58
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib
import urllib2

values={"username":"test@qq.com", "password":"test"}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
print geturl
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
