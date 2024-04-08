class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self._name = 9
       
    # 当实例对象找不到属性时调用该函数
    def __getattr__(self, name):
        print("test3")
        
        return getattr(self._obj, name)
    # 每次设置属性时都会调用这个方法，不管属性是否已经存在。
    def __setattr__(self, name, value):
        if name.startswith('_'):
            print(9)
            #调用父类的__setattr__函数
            super(Proxy,self).__setattr__(name, value)
            
        else:
            setattr(self._obj, name, value)
    
    #读时一定先调用此属性，
    #如果属性存在，它会直接返回；如果实例没有该属性，
    # 那么会检测我们是否定义了 __getattr__，定义了则执行，
    # 没定义则抛出 AttributeError。我们将这两个方        a
    def __getattribute__(self, __name: str):
        if __name in  ["age","name"]:
            raise ValueError("禁止访问")
        else:
            print("test")
           
            return super(Proxy,self).__getattribute__(__name)
class A():
    pass
   # nam = 8     
p = Proxy(A())
p._name = "test"
p.nam
#p.xx

"""
抱歉最近心情极差，忘了更新。

整个执行顺序：
1.创建对象后先执行构造函数， self._obj = obj语句第一次触发
 __setattr__函数输出“9”，接着执行 self._name = 9
语句第二次触发__setattr__再次输出“9”
接着执行p._name = "test"，第三次触发__setattr__输出“9”
2.执行p.nam,触发 __getattribute__输出“test”，因为没有定义nam属性
会__getattr__，所以输出test3，其中的self._obj语句会再次触发__getattr__
然后输出test，因为obj上并没有该属性，所以最终报错。

    """
