# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:35:03 2015

@author: Taikor
"""

from pynlpir import nlpir
import os

#pynlpir.nlpir.ImportUserDict(r'C:\workspace\20141230101836_ICTCLAS2015\ICTCLAS2015\bin\ICTCLAS2015\userdic.txt')

def find_NewWords(file):
    nlpir.Init(nlpir.PACKAGE_DIR, nlpir.UTF8_CODE, None)
    with open(file, 'r', encoding='utf-8') as f:
        s = f.read()
    #c_string = ctypes.c_char_p(id(s))
    #result = pynlpir.segment(s, pos_tagging=True,pos_names="all")
    new_words = nlpir.GetNewWords(s.encode(), 50, False).decode()
    
    #print(result)
    #print(new_words)

    if len(new_words) != 0:
        with open("new_words", 'a', encoding='utf-8') as f:
            f.write(new_words+'\n')
            print(new_words)

    nlpir.Exit()

folder_path = '有效'
path_list = os.listdir(folder_path)
for path in path_list:
    try:
        find_NewWords(folder_path + '\\' + path)
    except:
        pass

