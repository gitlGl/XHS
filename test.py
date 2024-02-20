#2023/12/08
#通过字符串形式导入模块
#知识1
import importlib
package_name1 = "numpy"
package_name2 = "xxx.xxx.xxx"
package = importlib.import_module(package_name1)
package = importlib.import_module(package_name2)

#还可以通过内置函数__import__导入
__import__("xxxx")#不支持"xxx.xxx.xxx"这种方式