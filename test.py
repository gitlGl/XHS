#2023/11/16
def my_function(a, b, *, c, d):
    print(a, b, c, d)

my_function(1, 2, c=3, d=4)  # 使用关键字参数调用函数

# 以下是错误的调用方式：
#my_function(1, 2, 3, 4)  # 错误！参数c和d必须使用关键字参数传递
#my_function(1, 2, 3, d=4)  # 错误！参数c必须使用关键字参数传递

def my_function(a, b, /, c, d):
    print(a, b, c, d)

my_function(1, 2, 3, 4)  # 使用位置参数调用函数
my_function(a = 1,b = 2, c=3, d=4)#错误，a,b必须使用位置参数传递

def my_function(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

my_function(1, 2, 3, 4, e=5, f=6)  # 可以使用位置参数和关键字参数
my_function(1, 2, c=3, d=4, e=5, f=6)  # 也可以全部使用关键字参数