# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:22:14 2015

@author: Taikor
"""

def dedup(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = list()
    for line in lines:
        pos_list = line.split('#')
        for pos in pos_list:
            if len(pos) > 0:
                new_lines.append(pos)
    
    dedupped_new_lines = set(new_lines)
    
    return '\n'.join(dedupped_new_lines)

file = "new_words"
s = dedup(file)
with open('clean_new_word', 'w', encoding='utf-8') as f:
    f.write(s)
                
    