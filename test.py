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