class lazyproperty:
    """
    有get和set，优先返回get的返回值;
    没有set，优先找dict;
    没有set和dict，返回get.
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            #保存结果值
            setattr(instance, self.func.__name__, value)
            return value

def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property#只有setter，只读不可写
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius
        
c = Circle(4.0)
c.radius#4.0

c.area#输出：Computing area 50.26548245743669
c.area#50.26548245743669

c.perimeter#Computing perimeter 25.132741228718345
c.perimeter#25.132741228718345

c.area = 25

"""
很多时候，构造一个延迟计算属性的主要目的是为了提升性能。 
例如，你可以避免计算这些属性值，除非你真的需要它们。
这里演示的方案就是用来实现这样的效果的，
只不过它是通过以非常高效的方式使用描述器的一个精妙特性来达到这种效果的。
        """