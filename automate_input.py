import os
import sys

def make_input(i):
	f = open(i, 'r')
	lines = f.readlines()
	f.close()

	ref = 1
	count = 1

	st0 = '%chk='+i[:-4]+'''.chk
%nprocshared=4
%mem=20GB
#p pop=(nbo6,savenbos) b3lyp/6-31g(d,p) empiricaldispersion=gd3bj nosymm int=ultrafine

Title Card Required

0 1
'''

	st = ''
	for line in lines[2:]:
		if len(line.strip().split()) == 1 :
			#print st
			ref = 1
			g = open(i[:-4]+'-'+str(count)+'.g16', 'w')
			g.write(st0+st+'\n')
			g.close()
			st = ''
			count += 1
			ref = 0
		if len(line.strip().split()) == 2:
			ref = 1
		if ref and len(line.strip().split()) == 4:
			st += line

	g = open(i[:-4]+'-'+str(count)+'.g16', 'w')
	g.write(st0+st+'\n')
	g.close()


for i in os.listdir('.'):
	if i[-4:] == '.xyz':
		make_input(i)
		break