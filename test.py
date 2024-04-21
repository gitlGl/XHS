import re

text = "hello 123 4567 89 101112 helloabcde FGHIJKLM nopqr world 234"
pattern1 = r"\d{3,5}"# 匹配3到5个数字
pattern2 = r"hello[a-zA-Z]{3,5}"# 匹配3到5个字母
pattern3 = r'(hello.\d{2})|(world.\d{2})'#两组匹配组
#‘.’表示任意一个字符，除了换行符 \n 
#*. 要求在任意字符后面跟着一个具体字符，而 .* 则可以匹配任意数量的任意字符，包括零个字符。
# *.hello,hello.*,hello.*hello

matches1 = re.findall(pattern1, text)
matches2 = re.findall(pattern2, text)
matches3 = re.findall(pattern3, text)

"""findall() 函数的设计原则之一是保留捕获组的结构，
以便于在返回的结果中准确反映匹配结果的组织和顺序。
即使一个捕获组没有匹配到任何内容，它仍然在正则表达式中占据一个位置，
因此在返回结果中也需要保留其对应的位置，
以确保返回的元组与正则表达式中捕获组的结构一致。
这种设计有助于保持结果的一致性，并提供了更多灵活性，
因为它允许在后续处理中更轻松地识别和处理每个捕获组的匹配结果，即使某些捕获组可能为空
"""


print(matches1,matches2,matches3)  # 输出匹配的数字列表
#['123', '4567', '10111', '234'] ['helloabcde'] 
# [('hello 12', ''), ('', 'world 23')]

match = re.search(pattern1, text)#返回第一个匹配项或None

print("Start position:", match.start())  # 匹配的起始位置
print("End position:", match.end())  # 匹配的结束位置
print("Span of the match:", match.span())  # 匹配的起始和结束位置的元组
print("Entire match:", match.group(0))  # 整个匹配的字符串
text = "hello 123 world 456"

def double(match):
    value = int(match.group())
    return str(value * 2)

new_text = re.sub(r'\d+', double, text)
print(new_text)  # 输出 hello 246 world 912

