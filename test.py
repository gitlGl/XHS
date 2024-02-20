#2023/11/16
import traceback,sys
def f1():
     raise TypeError("Type error")
try:
    f1()
    """
    #Exception（异常）：所有异常的基类,常见子类如下
    AttributeError，TypeError，ValueError，NameError
    IndexError，FileNotFoundError，ZeroDivisionError
    e为异常类型对象
    """
except Exception as e:
    exc_type, exc_val, exc_tb = sys.exc_info()
    tb = e.__traceback__
    #<class 'TypeError'> Type error <class 'traceback'>
    print(exc_type,exc_val,type(exc_tb))
    #True True True
    print(e is exc_val,tb is exc_tb,exc_val.__traceback__ is exc_tb)
    # 获取 traceback 对象
    tb1 = traceback.extract_tb(tb)
    #文件名，行号，所在函数，出错具体代码
    for filename, lineno, function, code in tb1:
        print(code)#f1()  raise TypeError("Type error")
    # 遍历 traceback 对象中的帧信息，
    #注意traceback生成是函数栈释放期间,
    # 新生成的traceback指向旧traceback
    while tb is not None:
        #注意：获取具体出错代码比较复杂，
        # 有兴趣可以看traceback.extract_tb函数实现
        lineno = tb.tb_lineno
        frame = tb.tb_frame
        filename = frame.f_code.co_filename
        function = frame.f_code.co_name
        print(f"File: {filename}, Line: {lineno}, Function: {function}")
        tb = tb.tb_next
def catch(exc_type, exc_val, exc_tb):
    ...
sys.excepthook = catch
#重定义excepthook可以自定义报错信息提示,#
#没被try捕获的异常最终会被catch捕获并且退出程序
print(sys.path)