23/10/10
# super其实是一个代理类，而不函数，super类可以简化为如下：                             
class Meta(type):
    def __new__(cls,name, bases, attrs):
        "cls 是Meta自身"
        #调用type.__new__返回一个MySuper对象
        return super(Meta,cls).__new__(cls,name, bases, attrs)
    def __call__(self, *args,**kwds):
        """self 是MySuper"""
        arg1,arg2 = args
        self.__self_class__ = arg1
        self.__self__ = arg2
        #调用type.__call__,返回一个MySuper实例
        #type.__call__调用MySuper中的new与init
        return super(Meta,self).__call__()
print(Meta.__mro__)
class MySuper(metaclass = Meta):
    __Flag = False
    def __init__(self):
        if not self.__Flag :
            self.__Flag = True
            return 
        mro = self.__self__.__class__.__mro__
        next_parent_class = mro[mro.index(self.__self_class__) + 1]
        next_parent_class.__init__(self.__self__)
        self.__Flag = False
    def __new__(cls): 
        if cls is MySuper:
           
            return object.__new__(cls)
        mro =cls.__mro__
        next_parent_class = mro[mro.index(MySuper.__self_class__) + 1]
        return next_parent_class.__new__(cls) 
       
       
class Base(object):
    pass
class A(Base):
    AAA = 999
    def __new__(cls) :
        return MySuper(A,cls).__new__(cls)
    
    def __init__(self):
        self.test2 = "test2"
        MySuper(A,self).__init__()
class B(Base):
    def test1(self):
        print("hello,world")

    def __new__(cls) :
       return MySuper(B,cls).__new__(cls)  
    
    def __init__(self):
        MySuper(B,self).__init__()      
class C(B,A):
    """
    __new__函数是静态函数，重写时也不需要static修饰
    super(C,cls).__new__(cls)，静态函数手动传参(保持一致性)
    """
    def __new__(cls)  :
       return MySuper(C,cls).__new__(cls)
    
    def __init__(self):
        MySuper(C,self).__init__()   
c = C()
print(c.AAA,c.test2,A.__mro__,Meta.__mro__)
c.test1()