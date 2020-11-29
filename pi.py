from random import random
from math import sqrt
from time import clock
d=10000000
h=0.0
clock()
for i in range(1,d+1):
    x,y=random(),random()
    di=sqrt(x**2+y**2)
    if di<=1.0:
        h=h+1
p=4*(h/d)
print("pi的值：{}".format(p))
print("运行时间：{:.5f}s".format(clock()))
