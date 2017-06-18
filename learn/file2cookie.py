#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 09:34:58
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import cookielib
import urllib2

# 创建MozillaCookieJar的实例
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# 创建请求的request
request = urllib2.Request('http://www.baidu.com')
response = opener.open(request)
print response.read()
