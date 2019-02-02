#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:14:58 2018

@author: christoffer
"""

import scipy as sc
import matplotlib.pyplot as plt

data1 = sc.array([1.57, 1.56, 1.66, 1.74, 1.75, 1.62, 1.63, 1.71, 1.57, 1.66, 1.56, 1.72, 1.66, 1.54, 1.58])
data2 = sc.array([1.68, 1.55, 1.62, 1.66, 1.61, 1.61, 1.58, 1.51, 1.75, 1.70, 1.61, 1.59, 1.68, 1.67, 1.53])
data1og2 = sc.append(data1, data2)

print(sc.mean(data1))
print(sc.mean(data2))
print(sc.mean(data1og2))

print(sc.std(data1))
print(sc.std(data2))
print(sc.std(data1og2))

plt.hist(data1og2[::2], bins = 10)
plt.show()