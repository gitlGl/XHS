#heapq.heappop() 函数总是返回最小的的元素,
#即最小堆，pop与 push会触发堆调整，
# 保证下一次pop返回的元素是最小的。
# pop与 push操作的时间复杂度均为 O(log n)。
#其实就是数据结构里的堆，还有堆排序也是用来了堆实现

import heapq
#具备优先级的队列
class PriorityQueue:
    def __init__(self):
        #里面保存的是元组，例如(-priority, index, item)
        self._queue = []
        #记录元素加入队列的顺序，用于确定优先级相同时pop出
        # 的是最先加入队列的元素，队列先进先出。
        self._index = 0

    def push(self, item, priority):
        #-priority保证返回的是优先级最高的元素
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        print(self._queue)

    def pop(self):
        
        result = heapq.heappop(self._queue)[-1]
        print(self._queue)
        return result
    
    
class Item:
     def __init__(self, name):
         self.name = name
     def __repr__(self):
         return 'Item({!r})'.format(self.name)
#数字越大优先级越高
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())#Item('bar')
q.pop()#Item('spam')
q.pop()#Item('foo')
q.pop()#Item('grok')