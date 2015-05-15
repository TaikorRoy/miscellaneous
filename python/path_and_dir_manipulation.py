# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:22:57 2015

@author: Taikor
"""

try:
	dirname = path.dirname(path.abspath(__file__))
	if sys.platform == 'win32':
		libsvm = CDLL(path.join(dirname, r'..\windows\libsvm.dll'))
	else:
		libsvm = CDLL(path.join(dirname, '../libsvm.so.2'))
  
def folder_parser(folder_path):
    file_names = os.listdir(folder_path)
    dirname = os.path.dirname(folder_path)
    files = list()
    for file_name in file_names:
        files.append(os.path.join(dirname, file_name))
    return files
        