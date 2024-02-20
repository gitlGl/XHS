#2024/01/17
#yield from
def gen():
    yield "test1"
    yield "test2"

def gen_from():
    yield from gen()
    yield "test3"
    
for item in gen_from():
    print(item)
 #Produces  test1 test2 test3 
 
 #数组扁平化 摘自python cookbook
from collections.abc import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2,"hello" ,[3, 4, [5, 6], 7], 8]
# Produces 1 2 hello 3 4 5 6 7 8
for x in flatten(items):
    print(x)