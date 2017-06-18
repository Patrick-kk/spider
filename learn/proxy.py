#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 19:57:01
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$


import urllib2

enalbe_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
