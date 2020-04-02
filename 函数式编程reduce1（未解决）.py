def add(x,y):
    return x+y;
from functools import reduce;
print(reduce(add,[1,2,3,4,5,6]));