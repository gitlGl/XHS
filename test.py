#2023/10/24#type hint
global_hin: str
class Test():
    class_hint :int
   
def test(func_hint: str) -> str:
    pass
     
print(Test.__annotations__)
print(globals()["__annotations__"])
print(test.__annotations__)