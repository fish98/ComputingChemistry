# coding:utf-8

from math import exp

def calculate(time):
    atomiclock = 0.00001

    k1 = 0.001
    k2 = 0.2
    k3 = 0.1
    k4 = 0.04

    ca = 1 
    cb = cc = cd = ce = 0
    da = db = dc = dd = 0

    count = time / atomiclock

    for piece in range(int(count)):
        da = ca - ca / exp(atomiclock * k1) 
        ca = ca / exp(atomiclock * k1)
        if cb == 0:
            cb = da 
        else : 
            db = cb - cb / exp(atomiclock * k2)  
            cb = da + cb / exp(atomiclock * k2)
            if cc == 0: 
                cc = db
            else:     
                dc = cc - cc / exp(atomiclock * k3) 
                cc = db + cc / exp(atomiclock * k3) 
                if cd == 0:
                    cd = dc
                else: 
                    dd = cd - cd / exp(atomiclock * k4)
                    cd = dc + cd / exp(atomiclock * k4)
                    if ce == 0:
                        ce = dd
                    else: 
                        ce = dd + ce
                        
    print("concentration of A: ", ca)
    print("concentration of B: ", cb)
    print("concentration of C: ", cc)
    print("concentration of D: ", cd)
    print("concentration of E: ", ce)

if __name__ =='__main__':
    
    print("answer for 5 s\n")
    calculate(5)

    print("\nanswer for 10 s\n")
    calculate(10)

    print("\nanswer for 15 s\n")
    calculate(15) 

    print("\nanswer for 20 s\n")
    calculate(20)

    print("\nanswer for 25 s")
    calculate(25)   

#
# Arthor: Jiongchi Yu
# Date: 2020.4.18
# 
