# coding:utf-8

def train(data,start_b,start_a,learning_rate,num_iter):
	b = start_b
	a = start_a

	for i in range(num_iter):
		b,a =gradient(b,a,data,learning_rate)
		print(b)
		print(a)

	return [b,a]

def gradient(tmp_b, tmp_a, data, learning_rate):

	b_gradient = 0
	a_gradient = 0

	N = float(len(data))

	for i in range(0,len(data)):
		x = data[i][0]
		y = data[i][1]
	
		b_gradient += -(2/N)*(y-((tmp_a*x)+tmp_b))
		a_gradient += -(2/N) * x * (y-((tmp_a*x)+tmp_b))

	new_b = tmp_b - (learning_rate * b_gradient)
	new_a = tmp_a - (learning_rate * a_gradient)
	return [new_b,new_a]    

if __name__ =='__main__':
	
	# data = [(100, 2.573), (200, 5.376), (300, 8.431), (400, 11.72), (500, 15.29), (600, 19.33)]
	data = [(1,3), (2,5), (3,7), (4,9), (5, 11)]

	learning_rate = 0.0001
	initial_b =0.0
	initial_a = 0.0
	num_iter = 1000

	[b, a] = train(data,initial_b,initial_a,learning_rate,num_iter)

	print(b)
	print(a)
#
# Arthor: Jiongchi Yu
# Date: 2020.4.11
# 
