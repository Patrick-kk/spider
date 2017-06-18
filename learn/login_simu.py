#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 09:56:02
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import cookielib
import urllib, urllib2

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie), httpHandler, httpsHandler)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
headers = [('User-Agent', user_agent)]
opener.addheaders = headers

postdata = urllib.urlencode({
    'username': '13699773893',
    'password': 'kangkang'
    })

loginURL = 'https://passport.csdn.net/account/login'

result = opener.open(loginURL, postdata)
print result.read()

'''
cookie.save(ignore_discard=True, ignore_expires=True)
listURL = 'http://write.blog.csdn.net/postlist'
request = urllib2.Request(listURL)
response = opener.open(listURL)
print response.read()
'''