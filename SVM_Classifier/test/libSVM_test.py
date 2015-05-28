# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:48:34 2015

@author: Taikor
"""

import sys
import os


sys.path.append(r'C:\workspace\SVM_Classifier\libsvm-3.20\python')

from svmutil import *

y, x = [1,-1,1], [[5,4,8],[-1,1,-8],[2,3,2]]

y, x = [1,-1,1], [{1:1,2:4,3:1},{1:-1,2:1,3:-1},{1:2,2:3,3:2}]

prob = svm_problem(y,x)

param = svm_parameter('-t 0 -c 4 -b 1')

m = svm_train(prob, param)

y, x = [-1,1,1], [{1:1,2:-2,3:-8},{1:3,2:2,3:8},{1:9,2:11,3:4}]

test = svm_predict(y, x, m)

print(test)