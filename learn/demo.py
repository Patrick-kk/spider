#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 17:02:25
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()
