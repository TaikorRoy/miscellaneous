# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:24:04 2015

@author: Taikor
"""

from lxml import etree
from io import StringIO

file = r'C:\workspace\化妆品电商\商品列表html.txt'

with open(file, 'r', encoding='utf-8') as f:
    s = f.read()
    
f = StringIO(s)
doc = etree.parse(f)

a = doc.xpath(r'//div[@class="proTit"]')


