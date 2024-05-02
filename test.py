"""
当处理大型数据结构、
嵌套结构或者需要清晰地显示数据时
 可以使用 pprint 模块来打印出数据结构。
 例如，爬虫返回json格式数据，使用pprint模块来打印出数据结构
 使得数据结构更易读
    """
import json
import pprint

# JSON 数据
json_data = """{"name": "John Doe", "age": 30, "city": 
"New York","friends": ["Alice", "Bob", "Charlie"]}"""

# 将 JSON 数据解析为 Python 字典
parsed_data = json.loads(json_data)

pprint.pprint(parsed_data)
#输出
{'age': 30,
 'city': 'New York',
 'friends': ['Alice', 'Bob', 'Charlie'],
 'name': 'John Doe'}