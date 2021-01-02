#import xlwt
import pandas as pd
import sys
import os


d = {}
for i in os.listdir('.'):
	if i[-5:] == '.xlsx':
		df = pd.read_excel(i)
		s = df.s.values

		for i in range (len(s)):
			if s[i] in d:
				pass
			else:
				d[s[i]] = 1

li = [float(i) for i in d]
li.sort()

fl = {}
for i in os.listdir('.'):
	if i[-5:] == '.xlsx':
		df = pd.read_excel(i)
		s = df.s.values
		

		for k in df:
			if k == s:
				continue
			val = df[k].values
			l = []
			for j in range (len(li)):
				if li[j] in s:
					ind = list(s).index(li[j])
					l.append(val[ind])
				else:
					l.append('-')
			fl[k] = l 

#print (fl) 


st = 's '
for i in fl:
	st+=i+' '
st+= '\n'
for i in range (len(li)):
	st += str(li[i]) + ' '
	for j in fl:
		st += str(fl[j][i])+' '
	st+='\n'

print st  










