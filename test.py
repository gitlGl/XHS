#2023/11/13#函数柯里化例子
def add(x, y, z):
    return x + y + z

def curry(fn):
    def curried(*args):
        if len(args) == 1:
            return lambda y: lambda z: fn(args[0], y, z)
        elif len(args) == 2:
            return lambda z: fn(*args, z)
        else:
            return fn(*args)
    return curried

@curry
def add_curried(x, y, z):
    return x + y + z

# 使用柯里化函数
one_plus_two = add_curried(1)
result = one_plus_two(2)
print(result)  # 输出 3

two_plus_three = add_curried(2)(3)
print(two_plus_three)  # 输出 5