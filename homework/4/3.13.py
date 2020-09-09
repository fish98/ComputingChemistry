# coding:utf-8

import numpy as np

if __name__ == '__main__':

    c = 12.01
    h = 1.008
    n = 14.01
    o = 16

    element = [12.01, 1.008, 14.01, 16]

    # following C - H - N - O

    compound = [[6, 5, 1, 2], [6, 7, 1, 0], [3, 7, 1, 1], [2, 6, 0, 1]]

    compoundAll = [6 * c + 5 * h + n + 2 * o, 6 * c + 7 * h + n + 0 * o, 3 * c + 7 * h + n + 1 * o, 2 * c + 6 * h + 1 * o]

    p = [0.5778, 0.0792, 0.1123, 0.2309]

    total = np.zeros((4,4), np.float)

    # init function

    for equation in range(4):
        for item in range(4):
           total[equation][item] = compound[item][equation] * element[equation] - p[equation] * compoundAll[item]
    
    for i in range(4):
        total[0][i] = 1

    # load data clear
    print(total)

    zero = np.array([1,0,0,0])
    
    # solve function
    # amount of substance

    answer = np.linalg.solve(total, zero)
    print (answer)

    # calculate all weight

    weight = 0
    for item in range(4):
        weight = compoundAll[item] * answer[item] + weight
    
    # generate weight ratio

    w_answer = np.zeros(4)
    for item in range(4):
        w_answer[item] = compoundAll[item] * answer[item] / weight 

    # print answer
    
    print(w_answer)

#
# Arthor: Jiongchi Yu
# Date: 2020.4.18
# 
