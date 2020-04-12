# coding:utf-8

import numpy as np
from scipy.optimize import leastsq

# 
# take init as initial  
#

def func(init):
    a, b = init
    return(y - (a * x + b))

def predict(a, b, x):
    return a * x + b

if __name__ =='__main__':

    x = np.array([100, 200, 300, 400, 500, 600])
    y = np.array([2.573, 5.376, 8.431, 11.72, 15.29, 19.33])

# get a and b parameter 

    a, b = leastsq(func, [1,2])[0]

# generate x output

    print("The simulation function is ΔH =", a, "* T", b)
    print("Predicted ΔH of 350℃ is", predict(a, b, 350))

#
# Arthor: Jiongchi Yu
# Date: 2020.4.11
# 
