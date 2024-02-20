#装饰器wraps的使用
import inspect
from functools import wraps
def test1(arg):
    """
    参数：arg
    """
    print(arg)

# 作用为是test1的元信息覆盖test2的元信息，
# 且test1函数即是test2.__wrapped__
# 等同于wraps(test1)(test2)
@wraps(test1)
def test2(arg1,arg2):
    """
    参数：
    arg1: 第一个参数
    arg2: 第二个参数
    """

test2.__wrapped__("test1")
print(globals())
test2_info = inspect.getdoc(test2)
print(test2_info)
#输出
"""
test1
参数：arg
"""
