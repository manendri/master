import os
import sys
#import sympy as sp
#from sympy import Symbol, solve
import numpy as np


f = open(sys.argv[1], 'r')
lines0 = f.readlines()
f.close()

cords, atoms = [], []
for line in lines0[3:]:
	k = line.strip().split()
	if len(k) < 4:
		continue

	atoms.append(k[0])
	cords.append(list(map(float, k[1:])))


g = open(sys.argv[2], 'r')
lines = g.readlines()
g.close()

ids = None
a,b,c = 0.0, 0.0, 0.0
for line in lines:
	k = line.strip().split('=')
	if len(k) < 2 or '%' in line:
		continue
	print (k)
	if k[0].strip() == 'atom':
		ids = eval(k[1])

	elif k[0].strip() == 'a':
		a = eval(k[1])

	elif k[0].strip() == 'b':
		b = eval(k[1])

	elif k[0].strip() == 'c':
		c = eval(k[1])

	elif k[0].strip() == 'shift':
		shift = eval(k[1])

#print (ids, a,b,c,shift)


for i in range (len(shift)):

	id = ids[i] - 1

	#print (i)
	x = cords[id]
	
	expr = shift[i][0]

	expr = expr.replace('a', 'np.array(aa)')
	expr = expr.replace('aa', str(a))


	if shift[i][0][0] == '-':
		expr = 'np.array(x) '+expr
	else:
		expr = 'np.array(x) +'+expr
	
	expr = expr.replace('x', str(x))
	
	expr = expr.replace('b', 'np.array(b)')
	expr = expr.replace('b', str(b))
	expr = expr.replace('c', 'np.array(c)')
	expr = expr.replace('c', str(c))
	#print (expr)
	#break

	soln = eval(expr)#.subs({x:[0,0,0], a:a, b:b, c:c})

	#soln = solve(expr)
	#print (soln)
	cords[id] = soln

st = ''.join(lines0[:3])

for j in range (len(cords)):
	#print (' '.join(list(map(str,[atoms[j]] + list(cords[j])))), 'afsl')
	st += ' '.join(list(map(str,[atoms[j]] + list(cords[j])))) + '\n'

g = open(sys.argv[1][:-4] + '_modified.xyz', 'w')
g.write(st)
g.close()