from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

"Subscriber(addr='jonesy@example.com', joined='2012-10-19')"
sub.addr
'jonesy@example.com'
sub.joined
'2012-10-19'

"""命名元组的一个主要用途是将你的代码从下标操作中解脱出来。 因此
，如果你从数据库调用中返回了一个很大的元组列表，通过下标去操作其中的元素， 
当你在表中添加了新的列的时候你的代码可能就会出错了。
但是如果你使用了命名元组，那么就不会有这样的顾虑。"""

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

"""命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存空间。
如果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效。"""

#Best practices
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total



