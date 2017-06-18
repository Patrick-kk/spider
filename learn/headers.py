#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 19:48:24
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib
import urllib2

url = 'https://www.zhihu.com/#signin'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
values = {'username':'test', 'password':'test'}
headers = {'User-Agent':user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

print page
