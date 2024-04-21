
#从字典中提取子集
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 速度较慢，与字典推导比差距大概慢1-2倍

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
#&表示取交集
p2 = { key:prices[key] for key in prices.keys() & tech_names }

#速度快
p1 = {key: value for key, value in prices.items() if value > 200}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}