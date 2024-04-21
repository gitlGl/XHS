#集合的差集与交集运算
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.difference(set2)) #差集运算   输出：{1, 2, 3}
print(set1.__and__(set2))#交集运算
print(set1 - set2)  #差集运算 输出：{1, 2, 3}
print(set1 & set2)
print(set1.union(set2))#并集运算

# 集合的子集与超集运算
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

print(set1.issubset(set2))  # 子集运算 ，输出：    False
print(set1 <= set2)

print(set1.issuperset(set2))  #超集运算 输出：True
print(set1 >= set2)

#自定义对象支持交集、差集和子集运算，超集，并集运算
class MySet(set):
    def __and__(self, other):#交集运算
        return MySet(set.intersection(self, other))

    def __sub__(self, other):#差集运算
        return MySet(set.difference(self, other))

    def __le__(self, other):#子集运算
        return set.issubset(self, other)
    
    def __ge__(self, other):#超集运算
        return set.issuperset(self, other)
    
    def __or__(self, other):#并集运算
        return MySet(set.union(self, other))
        
set1 = MySet([1, 2, 3, 4, 5])
set2 = MySet([1, 2, 3])

print(set1 & set2)  # 交集 输出：MySet({1, 2, 3})
print(set1 - set2)  # 差集 输出：MySet({4, 5})
print(set1 <= set2)  #子集 输出：False
print(set1 >= set2)  # 超集输出：True
print(set1 | set2)  #并集 输出：MySet({1, 2, 3, 4, 5})





