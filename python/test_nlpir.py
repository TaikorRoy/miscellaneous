# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:35:03 2015

@author: Taikor
"""

from pynlpir import nlpir
import ctypes

nlpir.Init(nlpir.PACKAGE_DIR, nlpir.UTF8_CODE, None)

#pynlpir.nlpir.ImportUserDict(r'C:\workspace\20141230101836_ICTCLAS2015\ICTCLAS2015\bin\ICTCLAS2015\userdic.txt')

path = 'C:\\Users\\Taikor\\Desktop\\raw_txt_sample.txt'

with open(path, 'r', encoding='utf-8') as f:
    s = f.read()

#c_string = ctypes.c_char_p(id(s))
#result = pynlpir.segment(s, pos_tagging=True,pos_names="all")
new_words = nlpir.GetNewWords(s.encode(), 50, False).decode()

#print(result)
print(new_words)

nlpir.Exit()