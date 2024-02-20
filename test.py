#2023/11/28
import copy
#浅拷贝,只进行浅层拷贝，嵌套对象不拷贝
items = [1, ['foo', 'bar'], 2, 3]
items_copy = copy.copy(items)
items_copy[0] = 100 
items_copy[1].append('xxx') 
#不影响原对象浅层对象，改变嵌套对象
print(items)#[1, ['foo', 'bar', 'xxx'], 2, 3]

#深拷贝，层层拷贝
items = [1, ['foo', 'bar'], 2, 3]
items_copy = copy.deepcopy(items)
items_copy[0] = 100 
items_copy[1].append('xxx') 
#不影响原对象，包括嵌套
print(items)#[1, ['foo', 'bar'], 2, 3]
