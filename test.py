#2024/01/16
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
#切片中的数字严格说属于硬编码，如果可以尽量使用切片对象
#提高代码可读性和可维护性
SHARES = slice(20, 23)
PRICE = slice(31, 37)
print(SHARES.start,SHARES.stop,SHARES.step)#0 23 20 None
cost = int(record[SHARES]) * float(record[PRICE])

a = slice(5, 50, 2)
s = 'HelloWorld'

# indices(size) 方法将它映射到一个确定大小的序列上， 
# 这个方法返回一个三元组 (start, stop, step) ，
# 所有值都会被合适的缩小以满足边界限制， 
# 从而使用的时候避免出现 IndexError 异常
b = a.indices(len(s))#(5, 10, 2)
for i in range(*a.indices(len(s))):
    print(s[i])