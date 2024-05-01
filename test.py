"""
可以进行比较的内置类型有：
1.数字类型（整数、浮点数和复数）
2.字符串
3.元组
4.列表
5.集合：集合运算
6.字典：只能比较相等性
    """
#比较背后的unicode代码点
"gh" > "gj的"

#首先取列表中的第一个元素即元组进行比较，两个原组比较，
#取元组中的第一个元素比较，因为第一个元素相同，所以比较第二个元素，返回False
[(1, 2)] > [(1, 8)] 

#比较需要同类型间的比较,
# 报错TypeError: '>' not supported between instances of 'tuple' and 'int'
[(1, 2)] >  [1,(1, 8)]

my_list = [((7,34,568),1, 5), ((7,55),1000, 2), ((7,),7, 8)]

max_tuple = max(my_list)#将列表中的元素进行比较，返回最大的元组
print(max_tuple)  # ((7, 55), 1000, 2)

#也可以通过key参数指定比较的元素，元组的作用是多级比较
#reverse:默认为False，表示升序排列，为True表示降序排列
max_tuple = max(my_list, key=lambda x: (x[1],x[0] ))
my_list = sorted(my_list,key=lambda x: (x[1],x[0] ),reverse= True)

#[((7, 34, 568), 1, 5), ((7,), 7, 8), ((7, 55), 1000, 2)]
print(my_list) 

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}
# 在字典中使用max()和min()，sorted函数
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))

data = [[123, 4838, 3, 5], [1, 4, 3, 67]]
# 对每个子列表原地排序
for sublist in data:
    sublist.sort()
