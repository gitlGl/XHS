#作为新手写过的迷惑代码
#numbers 的索引为0-4
numbers = [1,5,8,4,10,7]

#切片后产生新的列表对象，列表内容只是引用，切片复制了列表，
# remove删除了列表中对象的引用
print(numbers[:] is numbers)
#前面说过迭代器，num的值实质也是通过索引获取
for num in numbers[:]:
    if num %2 == 0:
        #删除操作后索引变化，假设删除8
        #则索引变为0-3（[1,5,4,10]），
        # 而迭代器中的索引仍然为0-4
        #则下一个num的值为numbers[3],4被跳过
        numbers.remove(num)

print(numbers)#输出：[1, 5, 4]