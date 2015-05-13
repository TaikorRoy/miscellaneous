# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:46:11 2015

@author: Taikor
"""

import os
import random
import shutil

folder_path = r'crop\有效'

files = os.listdir(folder_path)

random.shuffle(files)

samples = files[0:6000]

new_folder_path = r'corpos\有效（抽样）'

if not os.path.isdir(new_folder_path):
    os.mkdir(new_folder_path)

for sample in samples:
    shutil.copyfile(folder_path + '\\' + sample, new_folder_path + '\\' + sample)