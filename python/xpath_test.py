# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:24:04 2015

@author: Taikor
"""

from lxml import etree
from io import StringIO
"""
file = r'C:\workspace\化妆品电商\商品列表html.txt'

with open(file, 'r', encoding='utf-8') as f:
    s = f.read()
    
f = StringIO(s)
doc = etree.parse(f)
"""


s = u'<html><div class="proTit bbp">a我a<span>TTT<em>GGG</em></span>abc</div></html>'
f = StringIO(s)
doc = etree.parse(f)
a = doc.xpath(r'//div[@class="proTit bbp"]')
r = a[0].xpath(r'text()')
print(r)

"""
query = dict()
query["sku_name"] = u'我是'
query["size"] = '400'
query["category"] = 2
query["B2C_platform"] = '1'

condition = [x+"='"+unicode(y)+"' AND " for x, y in query.items()]

"""






