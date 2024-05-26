"""yield from 后面可以接一个可迭代对象。
当你使用 yield from 语句时，

你实际上是在告诉 Python：“我想从这个可迭代对象中逐个取出值，
并在我的生成器中产生它们”。

这不仅仅限于生成器，还可以是任何可迭代对象，
比如列表、元组、字典视图（如 dict.keys()、dict.values()、dict.items()）、
集合、字符串，甚至是文件对象（如果它们支持迭代）。
"""
def outer_generator(n):  
    yield from inner_generator(n) 
        
def inner_generator(j):  
    yield from [1,range(2),3]
  
# 使用嵌套生成器  
for  k in outer_generator(3):  
    print(k)
    
def gen1():  
    yield 1  
    yield 2  
  
def gen2():  
    yield from [3, 4, 5]  
    yield from gen1()  # 嵌套使用 yield from  
  
def gen3():  
    yield 'a'  
    yield from gen2()  # 再次嵌套使用 yield from  
  
# 使用 gen3  
for item in gen3():  
    print(item)