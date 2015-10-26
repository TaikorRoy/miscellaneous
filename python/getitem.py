__author__ = 'Taikor'

import time

class Test:
    def __getitem__(self, item):
        if item == 0:
            return '111'
        if item == 1:
            return '222'

a = Test()
print(a[0])