#!/usr/bin/env python
'''For N=10**20:
real    76m52.371s
user    76m48.884s
sys     0m0.036s'''
from __future__ import print_function
from __future__ import division
import math

#N=10**20
N=2**50
E=int(math.ceil(math.sqrt(N)))
s=[]

for i in xrange(2,E+1):
    dm = divmod(N, i)
    if dm[1] == 0:
        #print(i, dm[0])
        s.append((i,dm[0]))
#print(sorted(s))
print(s)
