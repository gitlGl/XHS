import xmltodict
import pprint
# 定义XML字符串
xml_data = '''
<bookstore>
        <book category="COOKING">
                <title lang="en">Everyday Italian</title>
                <author>Giada De Laurentiis</author>
                <year>2005</year>
                <price>30.00</price>
        </book>
        <book category="CHILDREN">
                <title lang="en">Harry Potter</title>
                <author>J K. Rowling</author>
                <year>2005</year>
                <price>29.99</price>
        </book>
        <book category="WEB">
                <title lang="en">Learning XML</title>
                <author>Erik T. Ray</author>
                <year>2003</year>
                <price>39.95</price>
        </book>
</bookstore>
'''

# 将XML转换为dict对象
data_dict = xmltodict.parse(xml_data, dict_constructor=dict)

# 将dict对象转换回XML
xml = xmltodict.unparse(data_dict, pretty=True)
print(xml)
#写入文件
with open('data.xml', 'w') as f:
    f.write(xml)
    
#从文件中读出并转换为字典
with open('data.xml', 'r') as f:
    xml = f.read()
    
data_dict = xmltodict.parse(xml, dict_constructor=dict)
pprint.pprint(data_dict)
{'bookstore': {'book': [{'@category': 'COOKING',
                         'author': 'Giada De Laurentiis',
                         'price': '30.00',
                         'title': {'#text': 'Everyday Italian', '@lang': 'en'},
                         'year': '2005'},
                        {'@category': 'CHILDREN',
                         'author': 'J K. Rowling',
                         'price': '29.99',
                         'title': {'#text': 'Harry Potter', '@lang': 'en'},
                         'year': '2005'},
                        {'@category': 'WEB',
                         'author': 'Erik T. Ray',
                         'price': '39.95',
                         'title': {'#text': 'Learning XML', '@lang': 'en'},
                         'year': '2003'}]}}