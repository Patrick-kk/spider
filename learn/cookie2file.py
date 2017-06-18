#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 09:27:08
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import cookielib
import urllib2

# 设置保存cookie的文件，统计目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 创建一个请求，原理同urllib2的urlopen
response = opener.open('http://www.baidu.com')
# 保存cookie到文件
#ignore_discard: save even cookies set to be discarded. 
#ignore_expires: save even cookies that have expired. The file is overwritten if it already exists
cookie.save(ignore_discard=True, ignore_expires=True)
