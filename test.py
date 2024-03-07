"""
python中的依赖安装特别麻烦，有些项目中缺乏依赖文件，或者依赖文件不清晰
提供两个方法导出依赖为 requirements.txt 文件

方法二一：
安装pipreqs，pip install pipreqs
然后执行命令：pipreqs ./ --encoding=utf8，
注意，pipreqs ./ 命令默认为系统编码格式。


方案二：
在pycharm上，找到Tool工具，选择Sync Python Requirements，导出项目依赖


"""
