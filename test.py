#字典视图的集合运算
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}

# 交集运算
intersection_keys = dict1.keys() & dict2.keys()
#values 不支持集合元素，因为集合元素需要可哈希，而字典的值不一定是可哈希的
#intersection_values = dict1.values() & dict2.values()
intersection_items = dict1.items() & dict2.items()

# 并集运算
union_keys = dict1.keys() | dict2.keys()
#union_values = dict1.values() | dict2.values()
union_items = dict1.items() | dict2.items()

# 差集运算
difference_keys = dict1.keys() - dict2.keys()
#difference_values = dict1.values() - dict2.values()
difference_items = dict1.items() - dict2.items()

keys = dict1.keys()#输出
print(keys)#dict_keys(['a', 'b', 'c'])
dict1['d'] = 4#添加一个键值对
#说明字典视图可实时更新
print(keys)#dict_keys(['a', 'b', 'c', 'd'])

"""dict_keys：键的视图。
dict_values：值的视图。
dict_items：键值对的视图。

字典视图（dictionary views）中的优势和用途：
1.动态性和实时更新：字典视图是动态的，它们会随着原始字典的更改而更新。
2.节省内存：字典视图并不会复制字典的数据，
3.可迭代性：字典视图是可迭代的，可以像迭代其他可迭代对象一样遍历它们。
4.支持集合操作：字典视图支持类似集合的操作，比如交集、并集、差集等。这使得你可以方便地对字典的键、
值或键值对进行集合运算，而无需显式地将它们转换为集合。
5.性能优化：在一些情况下，使用字典视图可以提高代码的性能。因为它们是动态的，不需要复制数据。
"""