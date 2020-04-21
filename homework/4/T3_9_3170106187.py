# coding:utf-8

def function(x):
    return 1 / (1 + x * x)

if __name__ =='__main__':

    n = 8

    wap = 1 / n
    total = 0

# Trapezoidal Algorithm
# Reach 1e-6 at n = 506 

    # for item in range(0, n):
    #     x1 = item * wap
    #     x2 = (item + 1) * wap
    #     part = (function(x1) + function(x2)) * wap / 2 
    #     total = total + part

# Simpson Algorithm
# Reach 1e-6 at n = 8

    base = 0
    for item in range(0, int(n/2)):
        x1 = (2 * item + 1) * wap
        x2 = (2 * (item + 1)) * wap
        base = base + 2 * function(x1) + function(x2)
    base = base * 2 + function(0) - function(1)
    total = wap / 3 * base

# Calculate pai 

    print(4 * total)

#
# Arthor: Jiongchi Yu
# Date: 2020.4.18
# 
