# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:32:31 2015

@author: Taikor
"""

import os
import random
import shutil

folder_path = r'corpos\排除（抽样）'

files = os.listdir(folder_path)

random.shuffle(files)

samples = files[0:3000]

new_folder_path = r'corpos\training_set\排除'

if not os.path.isdir(new_folder_path):
    os.mkdir(new_folder_path)

for sample in samples:
    shutil.copyfile(folder_path + '\\' + sample, new_folder_path + '\\' + sample)
    
samples = files[3000:6000]

new_folder_path = r'corpos\verification_set\排除'

if not os.path.isdir(new_folder_path):
    os.mkdir(new_folder_path)

for sample in samples:
    shutil.copyfile(folder_path + '\\' + sample, new_folder_path + '\\' + sample)