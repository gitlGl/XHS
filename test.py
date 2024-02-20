2023/12/13
class MyList:
    def __init__(self, items):
        self.items = items
        self.current_index = 0

    def __repr__(self):
        return f"MyList({self.items})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.items):
            current_item = self.items[self.current_index]
            self.current_index += 1
            return current_item
        else:
            raise StopIteration
        
#创建 MyList 对象
my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# 对 MyList 对象进行排序
sorted_list = sorted(my_list)

# 打印排序后的结果
print(sorted_list,my_list.items)

 
class Person:
    def __init__(self, name, age, friends):
        self.name = name
        self.age = age
        self.friends = friends

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, friends={self.friends})"

    def __lt__(self, other):
        return self.age < other.age

# 创建 Person 对象列表
people = [
    Person("Alice", 25, ["Charlie", "Bob"]),
    Person("Bob", 30, ["Charlie", "David"]),
    Person("Charlie", 20, ["Alice", "Bob"])
]

# 使用 sort() 函数对 Person 对象列表进行排序
people.sort()

# 打印排序后的结果
for person in people:
    print(person)
