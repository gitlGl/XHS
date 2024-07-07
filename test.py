import chardet

gbk = '你好，世界'.encode("gbk")
print(chardet.detect(gbk))
{'encoding': 'TIS-620', 
 'confidence': 0.22, 'language': 'Thai'}

utf8 = '你好，世界'.encode("utf8")
print(chardet.detect(utf8))
{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

"""
encoding: 表示检测到的文本编码名称。
confidence: 表示检测的置信度，范围从 0 到 1。
language: 表示检测到的文本所使用的语言。
    """