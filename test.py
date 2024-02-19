2023/11/13#自定义__repr__函数
class Person:
    def __init__(self, name, age,*args,**kw,):
        self.name = name
        self.age = age
        for key,value in kw.items():
            self.__dict__[key] = value
  
    def test(self):
        print("test")
    def __repr__(self):
        args = "" 
        for key,value in self.__dict__.items():
            if type(value) is str: 
                value = "'" + value + "'" 
            args = args + key + "=" + str(value) + ','
        return f"Person({args})"
    
str_p = Person("mc",67,7,lin = "test",).__repr__()
eval(str_p).test()#test