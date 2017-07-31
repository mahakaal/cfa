#continued fraction algorithm

from __future__ import division #for python 2.7
import math

i = 0
a = input("insert a : ")
b = input("insert b : ")

x = []
q = []

x.append(a/b)
q.append(math.floor(x[0]))

while q[i] != x[i]:
    x.append(1/(x[i] - q[i]))
    q.append(math.floor(x[i+1]))
    print str(i) + ": " + str(x[i]) + "--" + str(q[i])
    i = i + 1

q
