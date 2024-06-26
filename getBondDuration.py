#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:26:52 2024

@author: jiaruijia
"""

import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    t = np.arange(1, ppy*m+1)
    cpn = couponRate * face / ppy
    dft = np.array([(1 + y)**(-i) for i in t])
    dft_N = (1 + y)**(-ppy*m)
    P = getBondPrice(y, face, couponRate, m, ppy)  
    BondDuration= np.sum(t * cpn * dft / P) + m * face * dft_N / P
    return(BondDuration)

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10