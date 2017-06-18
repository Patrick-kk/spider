#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 20:36:21
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# 尾标签删掉了，是不闭合的
# 不过，lxml 因为继承了 libxml2 的特性，具有自动修正 HTML 代码的功能

html = etree.HTML(text)
result = etree.tostring(html)
print html

