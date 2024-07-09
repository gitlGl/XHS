import locale,sys
#返回一个元组，'zh_CN语言区域，
# 'cp936'即gbk
locale.getdefaultlocale() #('zh_CN', 'cp936')

#获取系统的首选编码，即系统默认的文本编码方式
locale.getpreferredencoding()#cp936

#获取 Python 解释器默认使用的文本编码。
sys.getdefaultencoding()#'utf-8'

#解释器默认utf8，若你的py文件是gbk且含有
#中文字符，则需要在文件开头注明gbk编码“# -*- coding: gbk -*-”
#否则报错SyntaxError: Non-UTF-8 code starting with “xxx”

print(len('你好， 世界。'.encode("utf8")))#19
print(len('你好， 世界。'.encode("gbk")))#13

"""
大多数计算机专业人士学习的第一门编程语言是c语言
而且在windows平台下经常遇到输出乱码情况，
多数情况是因为你.c文件保存的格式为
非gbk，而输出终端默认gbk，解决办法有两个：

1.把你的.c文件编码格式更改为gbk格式
2.gcc -fexec-charset=GBK -o hello hello.c
添加的‘-fexec-charset=GBK’表示把字符串常量处理为gbk编码格式

python终端输出则不会出现乱码情况，因为输出终端时python会
获取终端的编码格式，然后转换为终端的的编码格式，
python易学一定程度也是以为这些贴心的细节处理到位的。
    """
   