# coding:utf-8

import math
from decimal import *
# 
# Another algorithm to generate answers to a specific function
#

def test(x, t):
	return (-pow(10, t) - 1 + x) * x + pow(10, t)
	
def main():

#
# Calculate quadratic equation solutions 
# x^2 + (-10^t - 1)x + 10^t = 0
#

	t = int(input("Enter t\n"))
	a = 1
	b = -1 * pow(10, t) - 1
	c = pow(10, t)

#
# Limit is used for precise calculation
#

	limit = pow(10, -25)

#
# Settle starting point as -b/2a
# prerequisites as function exist 2 real number solution
#

	start = x1 = x2 = -((b + 1) / 2 / a)

#
# Start searching
#	
	# step = c / 2
	# while(step != limit): 
# Start from larger end
		# compare = round(test((x2+step), t) / test(start, t))
		# if compare > 0:
		# 	x2 = x2 + step
		# elif compare == 0:
		# 	x2 = x2 + step
		# 	break 
		# else: 
		# 	step = step / 10

# Reinit step
	step = c 
	while(step != limit):
# Search for another end
		compare = test((x1-step), t) / test(start, t)
		if compare > 0:
			x1 = x1 - step
		elif compare == 0:
			x1 = x1 - step
			break 
		else: 
			step = step / 10

	x2 = Decimal(c) / Decimal(x1)

	print("Solution x1 = %d" % x1)
	print("Solution x2 = %d" % x2)

if __name__ == '__main__':
	main()

#
# Arthor: Jiongchi Yu
# Date: 2020.3.29
# 
