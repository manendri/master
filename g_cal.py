import numpy as np
import sys
f=open(sys.argv[1],'r')
lines=f.readlines()
f.close()

x,y=[],[]
for line in lines:
	args=line.strip().split()
	x.append(float(args[0]))
	y.append(float(args[1]))

def gradient(x,y,order):
	g=y
	for i in range (order):
		g=np.gradient(g,x)
	return g
	
grad=gradient(x,y,1) # 1 is for first derivative
for i in grad:
	print i




