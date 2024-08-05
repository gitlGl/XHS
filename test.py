import pandas as pd

# 创建示例DataFrame
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value1': [1, 2, 3, 4]})

df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value2': ['foo', 'bar', 'baz', 'qux'],
                     'value3': ['foo', 'bar', 'baz', 'qux']}
                   )


# 使用 pd.merge 合并特定列
merged = pd.merge(left=df1[['key']], right=df2[['key', 'value2',
                                'value3']],on='key', how='left')
print(merged)


# 创建示例DataFrame
df1 = pd.DataFrame({'key_left': ['A', 'B', 'C', 'D'],
                    'value1': [1, 2, 3, 4]})

df2 = pd.DataFrame({'key_right': ['B', 'D', 'E', 'F'],
                    'value2': ['foo', 'bar', 'baz', 'qux']})

# 使用 left_on 和 right_on 合并特定列
merged = pd.merge(left=df1, right=df2, left_on='key_left',
                  right_on='key_right', how='inner')
print(merged)




df1 = pd.DataFrame({'key': ['A', 'B', 'C'],
                    'value1': [1, 2, 3]})

df2 = pd.DataFrame({'key': ['B', 'C', 'D'],
                    'value2': ['foo', 'bar', 'baz']})
merged = pd.merge(df1, df2, on='key', 
                  how='outer', indicator=True)
print(merged)



df1 = pd.DataFrame({'key': ['A', 'B', 'C'],
                    'value': [1, 2, 3],
                    'common_col': ['X1', 'Y1', 'Z1']})

df2 = pd.DataFrame({'key': ['B', 'C', 'D'],
                    'value': [4, 5, 6],
                    'common_col': ['X2', 'Y2', 'Z2']})
merged = pd.merge(df1, df2, on='key', suffixes=('_df1', '_df2'))
print(merged)


# 多层索引示例
multi_index_df = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B'],
    'key2': ['X', 'Y', 'X', 'Y'],
    'data': [10, 20, 30, 40]
})

# 另一个多层索引示例
another_multi_index_df = pd.DataFrame({
    'value': [100, 200, 300, 400]
}, index=pd.MultiIndex.from_tuples([('A', 'X'), 
        ('A', 'Y'),('B', 'X'), ('B', 'Y')], names=['key1', 'key2']))

# 使用多层索引进行合并
merged_multi = pd.merge(multi_index_df, another_multi_index_df,
                        left_on=['key1', 'key2'], right_index=True)
print(merged_multi)

'''copy (bool, 默认为 True):
控制是否复制数据。当 copy=True 时，原始数据不受影响，
返回合并后的新DataFrame；当 copy=False 时，尝试在合并时直接修改原始数据，'''