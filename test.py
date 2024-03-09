import sys
print(sys.path)

['3.8.3\\python38.zip', 
'3.8.3\\DLLs', 
'3.8.3\\lib', 
'3.8.3', 
'3.8.3\\lib\\site-packages',
'3.8.3\\lib\\site-packages\\win32',
'3.8.3\\lib\\site-packages\\win32\\lib',
'3.8.3\\lib\\site-packages\\Pythonwin']
" python -m http.server",'python -m venv myenv'#请看图二图三文件夹
#使用python的时候偶尔会用到"python -m xxx",多数人应该不知道“-m”参数的原理
#"m"表示module，即模块，带上-m参数的命令会去sys.path中的路径去补全完整路径
#一个模块通常使用__init__.py文件去暴露接口提供给第三方使用。