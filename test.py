import unicodedata,sys
def print_all_categories():
    categories = set()
    for i in range(sys.maxunicode):  # 遍历 Unicode 中的所有代码点
        category = unicodedata.category(chr(i))
        categories.add(category)
    print("所有的 Unicode 分类:")#中文字符通常归类为‘Lo’：其他字母。
    print(sorted(categories))

print_all_categories()

s = ' hello world \n'
s.strip()
'hello world'
s.lstrip()#去除左边
'hello world \n'
s.rstrip()#去除右边
' hello world'

t = '-----hello====='
t.lstrip('-')
'hello====='
t.strip('-=')#去除左边指定字符
'hello'

s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
     ord('\t') : ' ',
     ord('\f') : ' ',
     ord('\r') : None # Deleted
 }
a = s.translate(remap)
'pýtĥöñ is awesome\n'
#一般来讲，代码越简单运行越快。对于简单的替换操作，replace()通常是最快的
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

