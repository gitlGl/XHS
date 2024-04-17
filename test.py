xpts = [1, 5, 4, 2, 10, 7,10]
ypts = {101, 78, 37, 15, 62, 99}
for x, y in zip(xpts, ypts):#回元组 (x, y) 的迭代器,迭代长度跟参数中最短序列长度一致。
    print(x,y)
    
#代长度跟参数中最长序列长度一致
a=[1,2,3,4]
b=["yy","bb","tt"]
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)
    
for i in zip_longest(a, b, fillvalue=0):
    print(i)

    
t=[2,3,4]
g=["hh","cc","bb"]
f=[7.9,8,8]
for i in zip(t, g, f):
     print(i)

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in  a + b:
    print(x)
    
active_items = {1, 2, 3, 4}
inactive_items = ['x', 'y', 'z']
for item in chain(active_items, inactive_items):
    print(item) 
#a + b和chian()对比
# a + b,创建新的序列且要求a和b的类型一致,chian() 可迭代对象类型可不一样,且省内存