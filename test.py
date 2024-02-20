#base64编码例子
from base64 import b85decode,b85encode
def split_and_merge(text, char_limit=79):
    str_count = len(text)//char_limit
    end_str = text[str_count*char_limit:]
    #按指定长度将填充后的文本分割成行
    lines = [text[i:i+char_limit] for i in range(0, len(text), char_limit)]
    # 将所有行合并在一起，并在每行之间添加换行符
    final_text = '\n'.join(lines)
    return final_text


#读取需要编码的二进制文件然后编码
with open("desktop/test.zip","rb")  as f :
    data = f.read()
    encode_data = b85encode(data)

#编码后写入文本，然后记事本打开复制到本文件中，即是二进制变量DATA   
with open("desktop/test.txt","w+") as f:
#split_and_merge,每79个字符为一行插入换行符，
# b85不包括换行符，不会污染文件
    f.write(split_and_merge(encode_data.__repr__(),79))
#把DATA二进制变量解码后写入文件就能还原文件
with open("desktop/t.zip","wb") as f:
    f.write(b85decode(DATA.replace(b"\n",b'')))