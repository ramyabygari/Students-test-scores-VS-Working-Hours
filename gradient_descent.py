from numpy import *


def error_minimising(points,learning_rate,b,m):
	b_gradient=0
	m_gradient=0
	N=float(len(points))
	x=points[:,0]
	y=points[:,1]
	b_gradient += -(2/N) * (y - ((m * x) + b))
	m_gradient += -(2/N) * x * (y - ((m * x) + b))
	b_gradientsum=sum(b_gradient,axis=0)
	m_gradientsum=sum(m_gradient,axis=0)
	new_b=b-(learning_rate*b_gradientsum)
	new_m=m-(learning_rate*m_gradientsum)
	return new_b,new_m



def gradient_descent(points,starting_b,starting_m,learning_rate,num_iterations):
	x=points[0:80,0]
	y=points[0:80,1]
	print x
	print y

	b=starting_b
	m=starting_m

	for i in range(num_iterations):
		[b,m]=error_minimising(points,learning_rate,b,m)
		#print b
		#print m
	return [b,m]

def predict(points,b,m):
	x=points[81:100,0]
	y=points[81:100,1]
	for i in range(len(x)):
		y1=m*x[i]+b
		print ('predicted y=',y1)
		print('actual y=',y[i])
		print y[i]


def run():
	points=genfromtxt("/home/ramya/Desktop/DL/linear_regression_live/data.csv",delimiter=",")
	num_iterations=100000
	learning_rate=0.0001
	initial_b=0
	initial_m=0
	[b,m]=gradient_descent(points,initial_b,initial_m,learning_rate,num_iterations)
	prediction=predict(points,b,m)
if __name__=='__main__':
	run()
	