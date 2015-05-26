# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:21:03 2015

@author: Taikor
"""
import json

s = [{"brand":"\nabc"}]

a_s = json.dumps(s) 

    
str_a = a_s.replace('\n','')
