#2024/01/04

import hashlib
class HashDictionary:
    def __init__(self, initial_capacity=1000, load_factor=0.75):
        self.capacity = initial_capacity#初始容量
        self.load_factor = load_factor#平均每个位置元素大于0.75则扩容
        self.size = 0#统计数量
        self.hash_table = [None] * self.capacity

    def _get_hash(self, key):
        hash_val = hashlib.sha256(key.encode()).hexdigest()
        return int(hash_val, 16) % len(self.hash_table)
   
    def add(self, key, value):
        hash_index = self._get_hash(key)
        if self.hash_table[hash_index] is None:
            self.hash_table[hash_index] = (key, value)
            self.size += 1
            if self.size / self.capacity > self.load_factor:#触发扩容
                self._resize()
        else:
            hash_index = self._linear_probe(hash_index)#处理哈希冲突
            self.hash_table[hash_index] = (key, value)
            self.size += 1
            if self.size / self.capacity > self.load_factor:
                self._resize()
    def get(self, key):
        hash_index = self._get_hash(key)
        initial_index = hash_index
        i = 1
        while self.hash_table[hash_index] is not None:
            if self.hash_table[hash_index][0] == key:
                return self.hash_table[hash_index][1]
            hash_index = (initial_index + i) % len(self.hash_table)
            i += 1
            if hash_index == initial_index:
                break
        return None
    #续图二 
      
    #处理哈希冲突
    def _linear_probe(self, hash_index):
        initial_index = hash_index
        i = 1
        while self.hash_table[hash_index] is not None:
            hash_index = (initial_index + i) % len(self.hash_table)
            i += 1
        return hash_index

    def _resize(self):#扩容
        self.capacity *= 2
        new_hash_table = [None] * self.capacity
        for item in self.hash_table:
            if item is not None:
                key, value = item
                hash_index = self._get_hash(key)
                if new_hash_table[hash_index] is None:
                    new_hash_table[hash_index] = (key, value)
                else:
                    hash_index = self._linear_probe(hash_index)
                    new_hash_table[hash_index] = (key, value)
        self.hash_table = new_hash_table
    
hash_dict = HashDictionary()
hash_dict.add("apple", 10)
hash_dict.add("banana", 5)
hash_dict.add("orange", 7)

print(hash_dict.get("apple"))    # 输出: 10
print(hash_dict.get("banana"))   # 输出: 5
print(hash_dict.get("orange"))   # 输出: 7
print(hash_dict.get("grape"))    # 输出: None

hash_dict.add("apple", 20)       # 更新 "apple" 的值为 20
print(hash_dict.get("apple"))    # 输出: 20




#2024/01/05
import hashlib
key = "your_key"
hash_obj = hashlib.sha256(key.encode())
#大端，小端byteorder='big'/'little'
hash_val = int.from_bytes(hash_obj.digest(), byteorder='big')
print(hash_val)

def _get_hash(self, key):
    #hexdigest()作用是转化为16进制数字字符
    #int(hash_val, 16)16进制数字字符转为int
        hash_val = hashlib.sha256(key.encode()).hexdigest()
        return int(hash_val, 16) % len(self.hash_table)
    

import hashlib
key = "your_key"
# """
# 实际上哈希产生的是一串二进制，它既不表示数字，也不表示字符。
# 但是可以把这串二进制解释为数字或字符进行处理。
# ps：人类只能读数字或字符，读二进制太困难了，不过所有的所有都是数学

# "b'F]:2O\rB\xf9t\xba\x80\xb5\x03\xe7\xae\r'" 是一个由 Python 表示的字节字符串（bytes string）。
# 根据 ASCII 编码表，70 对应大写字母 'F'，93 对应字符 ']'，58 对应字符 ':'，50 对应字符 '2'，79 对应字符 'O'，
# 13 对应回车符 '\r'，66 对应大写字母 'B'，116对应"t"，\x加后面两个字符对应不可打印的特殊字符。
# 16进制，0-9，a-f，一共十六个个字符，每个字符只需要4位即可表示(半个字节)，即2的4次方。\x加后面两个字符表示一个字节。
# 除了\x外还有\u,表示万国码，万国码的范围是2的16次方，即表示一个万国码字符，需要16位两个字节，对应的是\u后面接四个
# 16进制字符，表示一个万国码字符。
# """
hash_obj = hashlib.md5(key.encode())
hex_string = hash_obj.hexdigest()#465d3a324f0d42f974ba80b503e7ae0d十六进制数字字符串表示
byte_string = hash_obj.digest()#b'F]:2O\rB\xf9t\xba\x80\xb5\x03\xe7\xae\r'#字符与十六进制数字字符表示

byte_string = b'F]:2O\rB\xf9t\xba\x80\xb5\x03\xe7\xae\r'
hex_string = byte_string.hex()#465d3a324f0d42f974ba80b503e7ae0d
print(hex_string)

x_string = ''.join(['\\x{:02x}'.format(b) for b in byte_string])
print(hex_string)#\x46\x5d\x3a\x32\x4f\x0d\x42\xf9\x74\xba\x80\xb5\x03\xe7\xae\x0d

print(int(hex_string, 16))#93530023678418335672200870123815808525

#大端，小端byteorder='big'/'little'，解释为数字时大端小端没关系，只要使用时统一即可。
hash_val = int.from_bytes(hash_obj.digest(), byteorder='big')
print(hex(hash_val))#0x465d3a324f0d42f974ba80b503e7ae0d

print(int.from_bytes(b"your_key",byteorder='big'))#8750341735091758457

num = 8750341735091758457
#num.bit_length()表示该数字所需的位数
K = 8 - num.bit_length()%8#向上取整
byte_array = num.to_bytes((num.bit_length() + K) // 8, 'big')
result = ''.join([chr(b) for b in byte_array])
print(result)#your_key
