# coding:utf-8

import numpy as np
from scipy import interpolate 

# 
# take init as initial  
#

if __name__ =='__main__':

    x = np.array([1.013, 1.539, 2.026, 2.533, 3.039, 3.546, 4.052])
    y = np.array([-0.50, 8.84, 18.07, 25.58, 31.80, 37.56, 42.61])

    linear1 = interpolate.interp1d(x, y, fill_value="extrapolate")
    
# print all the result of pressure -> temperature

    for index in range(1, 5):
        print("The boiling point under pressure", index, "Gpa is", linear1(index))

# print all the result of temperature -> pressure

# exchange data

    linear2 = interpolate.interp1d(y, x, fill_value="extrapolate")

    for index in range(0, 5):
        print((index*10), "Gpa pressure has", linear2(index*10), "boiling point")

#
# Arthor: Jiongchi Yu
# Date: 2020.4.11
# 