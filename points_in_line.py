import sys
import math


lis=eval(sys.argv[1])

def get_points(lis):
	[x1,y1,z1],[x2,y2,z2],d=lis
	m=(y2-y1)/(x2-x1)
	d-=1
	# line equation y=mx+c
	c=y1+((y2-y1)/(x2-x1))*x1 

	l=math.sqrt((y2-y1)**2+(x2-x1)**2)

	t=l*math.cos(math.atan(m))/d 

	tz=math.sqrt((x2-x1)**2+(z2-z1)**2)*math.cos(math.atan((x2-x1)/(z2-z1)))
	tz=tz/d 

	li=[]
	x=min(x1,x2)
	if x==x1:
		z=z1 
	else:
		z=z2 
	for i in range (d+1):
		X=x+i*t
		Z=z+i*tz
		li.append([X,m*X+c,Z])
	return li 

for a,b,c in get_points(lis):
	print a,b,c