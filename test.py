#2024/02/18
#不允许覆盖已存在的文件内容
import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
         f.write('Hello\n')
else:
    print('File already exists!')
    
"""
t是windows平台特有的所谓text mode(文本模式）,
区别在于会自动识别windows平台的换行符。
类Unix平台的换行符是\n，而windows平台用的是\r\n两个ASCII字符来表示换行，
python内部采用的是\n来表示换行符。
rt模式下，python在读取文本时会自动把\r\n转换成\n.wt模式下，
Python写文件时会用\r\n来表示换行。"""

#还有一个更好的方法，就是使用xt模式
#x模式是一个Python3对 open() 函数特有的扩展。 
# 在Python的旧版本或者是Python实现的底层C函数库中都是没有这个模式的。

try:
    with open('somefile', 'x') as f:
        f.write('Hello\n')
        
except FileExistsError as e:
    print("文件已存在")