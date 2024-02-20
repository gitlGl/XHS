2023/12/12
def my_generator():
        count = 0
        received_value = yield count
        print(f"Received value: {received_value,count}")
        count = count + 1
        received_value = yield count
        print(f"Received value: {received_value,count}")
        return "StopIteration finished"
           
gen = my_generator()
# 启动生成器
#next(gen)
gen.send(None)
# 启动生成器
next(gen)

try:
    next(gen)
except StopIteration as e:
    print(type(e),e)#<class 'StopIteration'> StopIteration finished
    #再来一次异常将返回异常值是None，而不是返回值StopIteration finished
    

#迭代生成器
gen2 = my_generator()
for item in gen2:
    #先判断gen是否已启动，若是第一次启动则直接运行到yield暂停，
    #并返回test,等待send，否则直接send，然后在代码yield处继续执行
    #直到再次遇到yield后返回test，然后等待send
    #for 循环会隐式捕获StopIteration 异常从而结束循环
    print(item)

