def gen():
    x = 0
    def inner():
        nonlocal x
        x = x + 1
        return x   
    return inner
    
g = iter(gen(),5)
# #使用iter()函数和partial函数创建了一个迭代器g，
# 该迭代器会重复调用gen()函数，直到返回的值等于5为止
for x in g:
    print(x)
    
#用于创建偏函数
RECORD_SIZE = 32
with open('test.bin', 'rb') as f:
    #如果返回b""，则表示迭代结束
    records = iter(partial(f.read, RECORD_SIZE), b'')
    #使用iter()函数和partial函数创建了一个迭代器records，该迭代器会重复调用
    for r in records:
        print(r)  

from functools import partial
#偏函数是指在调用函数时，固定函数的部分参数，从而创建一个新的函数
def add(a, b):
    return a + b*2

add_five = partial(add, 5)  # 不指定参数名，直接给定值 5
result = add_five(6)  # 调用 add_five 函数
print(result)  # 输出结果为 17

add_five = partial(add, b=5)
result = add_five(8) # 调用 add_five 函数
print(result) #输出结果为 18
