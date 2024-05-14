import xml.etree.ElementTree as ET
#https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html
xml = """<?xml version="1.0" encoding="UTF-8"?>
<config>
    <!-- 服务器配置 -->
    <server>
        <hostname>example.com</hostname>
        <port>8080</port>
        <protocol>https</protocol>
    </server>
    <!-- 数据库配置 -->
   <database attribute_name="attribute_value">
        <hostname>db.example.com</hostname>
        <port>3306</port>
        <username>admin</username>
        <password>password123</password>
    </database>
    <!-- 日志配置 -->
    <logging>
        <level>debug</level>
        <path>/var/log/myapp.log</path>
    </logging>
</config>
"""
with open('config.xml', 'w',encoding='utf-8') as f:
    f.write(xml)
    
import xml.etree.ElementTree as ET
# 读取XML文件
# ElementTree对象
#使用find属性时只支持查找element对象，不支持对element对象增删改查属性
tree = ET.parse('config.xml')

#Element对象
#使用find方法时xpath语法只能使用相对路径，支持对子element对象增删改查属性
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib,child.text)

# xpath简单语法
"""  . 表示当前节点(相对路径)，即 root，它在这里是 <config> 标签。
    /	从根节点选取（取子节点）。
    // 递归查找（取所有子节点）。
    .// 表示当前节点（相对路径）的所有子节点。"""

#选取所有具有属性attribute_name属性的节点，*代表所有元素节点
print(root.findall('.//*[@attribute_name]'))

#选取所有具有属性attribute_name属性的database节点
print(root.findall('.//database[@attribute_name]'))

#选取 database元素的所有子元素。
print(root.findall('./database/*'))

#递归获取所有元素
print(root.findall('.//'))

#获取当前元素
print(root.findall('.'))

#获取所有元素，不包括子元素
print("gs",root.findall('./'))

#选取 第一个database 元素。
print("fd",root.findall('./database[1]'))

#选取最后一个database 元素。
print("fd",root.findall('./database[last()]'))

#选取具有属性attribute_name属性的database元素。
root.findall(f'.//database[@attribute_name="attribute_value"]')

root.tag = 'cfj'#改变root 标签名

#tree.write('modified_config.xml',encoding='utf-8',xml_declaration=True)

#当前节点下子节点,'/server'旧版本使用方法
#新的使用方法为统一相对路径'./server'
print(tree.findall('./server'))
print(tree.findall('./'))



