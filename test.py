#摘自python cookbook
#2024/01/31 
import types
from functools import partial,wraps
class Test():
    pass

def hello(self):
    print("hello",self)
    
test = Test()

hello2 = types.MethodType(hello,test)
hello3 = partial(hello,test)

# #test.hello("test")AttributeError: 'Test' object has no attribute 'hello'
# hello2()#hello <__main__.Test object at 0x0000026B046CA820>
# hello3()#hello <__main__.Test object at 0x0000026B046CA820>

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
    
    #主要用于调整__call__函数中的self参数
    def __get__(self, instance, cls):
        if instance is None:#通过类名触发描述符时instance为None
            return self
        else:
            #这里实际绑定的是__call__函数
            return partial(self, instance)#types.MethodType(self, instance)
        
@Profiled#add别替换为描述符对象
def add(x, y):
    return x + y
class Spam:
    @Profiled#bar别替换为描述符对象
    def bar(self, x):
        print(self, x)
               
add(2, 3)#5
add.ncalls#1

s = Spam()
tem = s.bar#触发描述符
tem(7)#<__main__.Spam object at 0x0000026C5C158670> 7
tem2  = Spam.bar#通过类名触发描述符
tem(8)#<__main__.Spam object at 0x00000225DB988670> 8 
print(Spam.bar.ncalls) #2


#2024/01/30 摘自python cookbook，牛鼻的例子，大开眼界
from functools import wraps, partial
import logging
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel
            
        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')
    
import logging
logging.basicConfig(level=logging.DEBUG)
add(2, 3)#DEBUG:__main__:add
add.set_message('Add called')
add(2, 3)#DEBUG:__main__:Add called  
add.set_level(logging.WARNING)
add(2, 3)#WARNING:__main__:Add called

#2024/01/31 摘自python cookbook，牛鼻的例子，大开眼界
from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')           
def spam():
    print('Spam!')
    
add(2,45) #DEBUG:__main__:add
spam()#CRITICAL:example:spam  Spam!