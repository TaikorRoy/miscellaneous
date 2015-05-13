# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:57:04 2015

@author: Taikor
"""

import re
import os


def easy(folder_path):  
    files = os.listdir(folder_path)
    def strip_at(file):
        with open(file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
    
            for i in range(len(lines)):
                lines[i] = re.sub('@.+? |@.+?\n', '', lines[i])
            striped_lines = '\n'.join(lines)
            striped_lines.lstrip('\n')
        
        with open(file, 'w', encoding="utf-8") as f:       
            f.write(striped_lines)
    
    for file in files:
        strip_at(folder_path + '\\' + file)
        

folder_list = [r'C:\workspace\训练数据\训练结果测试\corpos\training_set\排除',
               r'C:\workspace\训练数据\训练结果测试\corpos\training_set\有效',
               r'C:\workspace\训练数据\训练结果测试\corpos\verification_set\排除',
               r'C:\workspace\训练数据\训练结果测试\corpos\verification_set\有效'           
               ]
               
for folder in folder_list:
    easy(folder)

