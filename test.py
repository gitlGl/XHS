numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

def custom_enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

for index, letter in custom_enumerate(letters, start=1):
    print(index, letter)

def custom_zip(*iterables):
    # 获取所有可迭代对象的迭代器
    iterators = [iter(iterable) for iterable in iterables]
    while True:
        try:
            items = [next(iterator) for iterator in iterators]
        except StopIteration:
            # 如果任何一个迭代器耗尽，则停止迭代
            return "StopIteration"
        else:
            yield tuple(items)

for item in custom_zip(numbers, letters):
    print(item)
    
def custom_chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

for item in  custom_chain(numbers, letters):
    print(item)