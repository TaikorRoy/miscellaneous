# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:14:12 2015

@author: Taikor
"""

verificationSet_feature = r'C:\workspace\训练数据\训练结果测试\华润分类器测试_v8.0\测试集\Feature.dic'
trainingSet_feature = r'C:\workspace\训练数据\训练结果测试\华润分类器测试_v8.0\训练集\Feature.dic'

def get_content(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines
    
def compare(*args):  
    verificationSet_lines = get_content(args[1])
    trainingSet_lines = get_content(args[0])
    
    count = 0
    for line in trainingSet_lines:
        if line in verificationSet_lines:
            count += 1
        else:
            pass
        
    return count
    
result = compare(trainingSet_feature, verificationSet_feature)
print(result)
            