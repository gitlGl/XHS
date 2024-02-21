#2024/02/01
class Profiled:
    def __init__(self, func):
        self.get = func
   
    def __get__(self, instance, cls):
       return self.get(instance)
        
    def __set__(self, instance, value):
            if not  hasattr(self, 'set'): 
                raise AttributeError("can't set attribute")
            return self.set(instance,value)
        
    def setter(self,func):
        self.set = func
        return self       
class Person:
    def __init__(self, name ,age):
        #self.name = name
        self.age = age
        self._name = None

    @Profiled
    def name(self):
        print("tttt")
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        self._name = value
   
    @Profiled
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be an int')
        self._age = value
        
p = Person("test",13)

print(p.age)#13
p.age = 27
print(p.age)#27


#print(p.name)#test
p.name = "test2"
print(p.name)#test2
