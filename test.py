#2024/01/06
#摘抄自python cookbook
from struct import Struct
data = [[123, 3.14, True],[123, 3.14, True]]
format = 'if?'
record_struct = Struct(format)

# 将二进制数据写入文件
with open('data.b', 'wb') as f:             
    for item in data:
        packed_data = record_struct.pack(*item)
        f.write(packed_data)

def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))
    
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

# Example
if __name__ == '__main__':
    with open('data.b','rb') as f:
        for rec in read_records(format, f):
            # Process rec
            ...
        data = f.read()
        for rec in unpack_records(format, data):
            ...
        # Process rec
        