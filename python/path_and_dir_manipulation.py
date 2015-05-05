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