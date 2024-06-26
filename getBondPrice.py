#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:16:39 2024

@author: jiaruijia
"""

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t=np.arange(0,ppy*m+1)
    df=(1/(1+y/ppy))
    cpn=couponRate*face
    dft=[df**i for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    return(bondPrice)

# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10


import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    coupon_payment = face * couponRate / ppy
    periods = np.arange(1, m*ppy + 1)
    discount_factors = (1 + y/ppy)**(-periods)
    pv_coupons = coupon_payment * discount_factors
    pv_face_value = face * discount_factors[-1]
    bond_price = np.sum(pv_coupons) + pv_face_value
    return bond_price


y = 0.03
face = 2000000
couponRate = 0.04
m = 10
