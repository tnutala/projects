# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:18:36 2018

@author: tnuta
"""

import numpy as np
import itertools

#generate Bn
n=3
n=np.arange(1,n+1)
print(n)
B7=np.array([])

for i in n:
    print(i)
    B7=np.append(B7,set(itertools.combinations(n,i)))
    
print(B7)
print()
