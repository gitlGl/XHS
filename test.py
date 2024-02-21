import json
from pprint import pprint
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
pprint(json_str)

# 把json数据文件写入文件中
with open('data.json', 'w') as f:
    json.dump(data, f)

# 从文件中读取json数据
with open('data.json', 'r') as f:
    data = json.load(f)
    
#json转为字典时保持数据顺序    
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)

print(data)
#OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])


#对象序列化与反序列化
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d


classes = {
    'Point' : Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d
    
    
    
p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
print(s)#'{"__classname__": "Point", "y": 3, "x": 2}'

a = json.loads(s, object_hook=unserialize_object)
print(a)#<__main__.Point object at 0x1017577d0>

