# coding:utf-8

# 
# Verify answers calculated by computer programs.
#

import math

def main():

#
# Calculate quadratic equation solutions 
# x^2 + (-10^t - 1)x + 10^t = 0
#

	t = int(input("Enter t\n"))
	a = 1
	b = pow(-10, t) - 1
	c = pow(10, t)

	x1 = (-1 * b + math.sqrt(b * b - 4 * a * c)) / 2 / a
	x2 = (-1 * b - math.sqrt(b * b - 4 * a * c)) / 2 / a

	print("Solution x1 = %d" % x1)
	print("Solution x2 = %d" % x2)

# 
# Note 
# Surprisingly found x2 equals 0 only when t is above 17 but not 11 in python
#

if __name__ == '__main__':
	main()

#
# Arthor: Jiongchi Yu
# Date: 2020.3.18
# 
