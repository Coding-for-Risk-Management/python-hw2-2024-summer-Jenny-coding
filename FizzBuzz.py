#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:34:41 2024

@author: jiaruijia
"""

import numpy as np

def FizzBuzz(start, finish):
    fbRange=np.arange(start,finish+1)
    mod3=np.mod(fbRange,3)
    mod5=np.mod(fbRange,5)
    mod3Zeros=np.where(mod3==0)
    mod5Zeros=np.where(mod5==0)
    
    FizzBuzz=[fbRange]
    FizzBuzz[mod3Zeros[0]]="Fizz"
    FizzBuzz[mod5Zeros[0]]="Buzz"
    FizzBuzz[mod3Zeros[0]] [mod5Zeros[0]]="FizzBuzz"
    return(FizzBuzz)



start = 1
finish = 15
numvec = np.arange(start,finish)
objvec = np.array(numvec,dtype = object)

# Tools: Append to a list

myEmptyList = []
for i in range(1,5):
    myEmptyList.append(i)
    
print(myEmptyList)




import numpy as np

def FizzBuzz(start, finish):
    arr = np.arange(start, finish + 1)
    result = np.empty_like(arr, dtype=object)
    result[:] = arr
    result[arr % 3 == 0] = 'Fizz'
    result[arr % 5 == 0] = 'Buzz'
    result[(arr % 3 == 0) & (arr % 5 == 0)] = 'FizzBuzz'
    
    return result

# Example usage:
start = 1
finish = 15
output = FizzBuzz(start, finish)
print(output)