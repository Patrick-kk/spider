#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 11:01:04
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib, urllib2

page = 1

url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.HTTPError, e:
    if hasattr(e, 'code'):
        print e.code
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print e.reason
