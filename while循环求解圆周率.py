#while循环求解圆周率
from random import random
from time import perf_counter
DARTS=2**25
hits=0
start=perf_counter()
i=1
while(i <=DARTS):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if(dist<=1):hits+=1
    i=i+1
pi=4*(hits/DARTS)
dur=perf_counter()-start
print("圆周率的值为：{:.2f}".format(pi))
print("程序运行的时间为：{:.2f}".format(dur))
