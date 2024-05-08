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
tree = ET.parse('config.xml')
root = tree.getroot()

# 修改服务器配置
"""  . 表示当前节点，即 root，它在这里是 <config> 标签。
    // 是一个XPath轴，表示选择从当前节点开始的文档中的所有位置，不限于子代，可以是任何后代节点。
    server 是我们要查找的标签名。
    .//server 表示选择所有名为 server 的标签，无论它们在文档中的什么位置。"""
for server in root.findall('.//server'):
      
    server.find('hostname').text = 'newhostname.com'
    server.find('port').text = '9090'

# 增加新的配置项
new_config = ET.Element('backup')
new_path = ET.SubElement(new_config, 'path')
new_path.text = '/var/backup'

# 将新配置项添加到根节点下
root.append(new_config)

#添加属性的节点
logging_elem = root.find('logging')
logging_elem.set('testattribute_name', 'attribute_value')

# 查找并删除具有指定属性值的节点
for elem in root.findall(f'.//database[@attribute_name="attribute_value"]'):
    print(elem)
    root.remove(elem)

tree.write('modified_config.xml',encoding='utf-8',xml_declaration=True)
