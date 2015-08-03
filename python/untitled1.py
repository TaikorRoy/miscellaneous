# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:21:21 2015

@author: Taikor
"""

import re
import codecs


def html_stripper(str_a):
    line = str_a
    patterns = ['' for i in range(5)]
    patterns[0] = r'<ahref.+?>'
    patterns[1] = r'<span.+?</span>'
    patterns[2] = r'<em.+?>'
    patterns[3] = r'</em>'
    patterns[4] = r'</a>'
    for pattern in patterns:
        line = re.sub(pattern, "", line, re.DOTALL)
    return line

with codecs.open(r"C:\workspace\WebCrawler\scrapy_workspace2\jumei\MianMo.json", "r", encoding="utf-8") as f:
    str_a = f.read()
    

line = html_stripper(str_a)

print(line)