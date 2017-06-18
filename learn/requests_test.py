#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 14:57:05
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import requests

r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
print r.text
print r.cookies
