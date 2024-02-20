#2024/02/16
import os
import mmap

size = 1000000
with open('data', 'wb') as f:
     f.seek(size-1)
     f.write(b'\x00')#前面被填充为b'\x00'

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)#为可读可写
    return mmap.mmap(fd, size, access=access)

# 打开文件并创建内存映射
with open("data", "r") as f:
    #获取文件描述符f.fileno()与上面fd一致
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print(type(m.readline()))
        

# 修改文件内容
with open("data", "r+") as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:
        m[0:5] = b"Hello"
        
#只能修改，不能删除，增加 。不能突破用户虚拟内存大小限制，必要时需要分块映射处理    
target_line = 3  # 要修改的行号
new_content = b'#test'  # 新的行内容

with open('test.py', 'r+') as file:
    with mmap.mmap(file.fileno(), 0,access=mmap.ACCESS_WRITE ) as mm:
        line_number = 0
        while True:
            line = mm.readline()
            if not line:
                break  # 已到达文件末尾
            line_number += 1
            if line_number == target_line:
                lenth = len(line)
                line_start = mm.tell() - lenth  # 计算第三行的起始位置
                line_end =  mm.tell() -1    # 计算第三行的结束位置
                
                content = new_content
                if  len(content)   > lenth -1 :
                    print("error")
                    break
                
                while len(content)   < lenth -1 :
                    content = content + b' ' 
              
            
                mm[line_start:line_end] = content    # 替换第三行的内容
                mm.flush()  # 将修改写回文件
                break