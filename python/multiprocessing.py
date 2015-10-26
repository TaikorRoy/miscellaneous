# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:24:42 2015

@author: Taikor
"""

from multiprocessing import Process
from multiprocessing import Pool
import time

def fib(n):
    sum = 0
    for i in range(n):
        sum += i
        sum = sum * 0.99
        for i in range(i):
            sum = sum - i*0.01
    return sum

 
a = time.time()

if __name__ == "__main__":
    pool = Pool(2)
    result = pool.map(fib, [12222,7111])
    print(result)    
b = time.time()
print(b-a)
