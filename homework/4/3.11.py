# coding:utf-8

import sympy as sp 

if __name__ == '__main__':

    a = sp.Symbol('x')    

    t = 3.24 * 3.04 * 3.04 * 0.1

    function = (t * (-4) - 4) * a**3 - (t * 12 + 12) * a**2 + (t * (-4) - 9) * a + t * 4
    a = sp.solve(function)
    
    print(a)

    print("the answer is")

    answer = a[2]

    print(answer / (3 - 2 * answer))



#
# Arthor: Jiongchi Yu
# Date: 2020.4.28
# 
