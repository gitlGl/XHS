#2024/01/07           
import locale,sys

default_encoding = locale.getpreferredencoding()
print(default_encoding,sys.getfilesystemencoding())

#2024/01/10
def convert_txt(f_mp4):
    bin_gen = iter(lambda: f_mp4.read(1024*10),b"")
    f_txt = open("01.txt","w",encoding="utf8")
    
    for bin in  bin_gen:
        #对bytes遍历返回的是int类型
        bin_str = ''.join(format(type_int,"b").zfill(8) for type_int in bin)
        f_txt.write(bin_str)
        
    f_txt.close()

def convert_mp4(f_txt):
    chunks = iter(lambda: f_txt.read(1024*10), '')
    f_mp4 = open('01.mp4', 'wb')
    
    for chunk in chunks:
        c8_list = [chunk[i:i+8] for i in range(0,len(chunk),8)]
        #to_bytes(1, byteorder='big')当第一个参数为1，且机器默认小端时，无论第二个参数是小端还是大端，均可取到低位字节。
        byte_gen = (int(c8, 2).to_bytes(1, byteorder='big') for c8 in c8_list )
        for byte in byte_gen:
            f_mp4.write(byte)
    
    f_mp4.close()
    
with open('test.mp4', 'rb') as f_mp4:
    # 读取文件内容为二进制数据
    convert_txt(f_mp4)
    
with open("01.txt","r",encoding="utf8") as f_txt :
    convert_mp4(f_txt)

n = 12345678960
K = 8 - n.bit_length()%8#向上取整
byte_count = (n.bit_length() + K) // 8
print(byte_count)  # 输出：2