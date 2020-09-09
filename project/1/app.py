# coding:utf-8

#
# Calculate possibilities
# Using brutal search
#

import time

def brutal(x, y):
	count = 0
	triad = '1' * x
	for i in range(pow(2,(y-1))):
		if triad in bin(i)[2:]:
			count += 1
	print("The possibility is : " + str(count/pow(2, (y-1))))

#
# Calculate possibilities
# Using recursive algorithm
#

def recursive(x, y):
	if x > y: 
		return 0
	elif x == y:
		return 1
	else:
		total = pow(2, y-x)
		for i in range(1, x+1):
			total += recursive(x, y-i)
		return total

#
# Main function
# Receive two input int for "X" continuous isotactic triad and "Y" units 
#

def main():
	x = int(input("Enter continuous isotactic triad number:\n"))
	y = int(input("Enter total units number:\n"))
	# Check whether X is smaller than Y-1  
	if x > y-1: 
		print("Isotactic triad number can not be bigger than total units number.")
		return
	else:
		# Algorithm selection

		# For brutal search, uncomment the line below
		brutal(x, y)
		
		# For recursive algorithm, uncomment the line below
		print("The possibility is : " + str(recursive(x, y-1)/pow(2, (y-1))))

if __name__ == '__main__':
	time_start=time.time()
	main()
	time_end=time.time()
	print('time cost',time_end-time_start,'s')

#
# Arthor: Jiongchi Yu
# Date: 2020.3.5
# 
