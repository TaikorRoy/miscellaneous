# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:18:14 2015

@author: Taikor
"""

with open("test_fseek", "rb+") as f:
    #f.write(b"my hero is here\nshe is there")
    f.seek(2, 0)
    f.write("@")
    