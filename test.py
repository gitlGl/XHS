 #2023/11/22
import sys,os
print(sys.path)
file_path = os.path.abspath(__file__)
path = os.path.dirname(file_path) 
#sys.path[0]与上面两行代码等价
print(path == sys.path[0])#输出True
print("工作目录：",os.getcwd())
#输出
"""
['c:\\Users\\Administrator\\Desktop\\XHS', 'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3\\python38.zip', 
'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3\\DLLs', 
'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3\\lib', 
'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3', 
'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3\\lib\\site-packages',
'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3\\lib\\site-packages\\win32',
'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3\\lib\\site-packages\\win32\\lib',
'C:\\Users\\Administrator\\.pyenv\\pyenv-win\\versions\\3.8.3\\lib\\site-packages\\Pythonwin']
True
工作目录： C:\Users\Administrator\Desktop\XHS
"""
"""
#path中的目录除了第一个属于用户输入以外，一是Python运行期间根据自身所在目录
作为相对目录生成，二是根据环境变量pythonpath生成
import sys,os
导包过程实际完整路径是
pyenv-win\\versions\\3.12.0\\Lib\\sys,os
python会根据sys.path中的路径去补全完整的导包路径
sys.path中的路径存在优先级，第一个是python 可执行文件所在路径
如果在此路径找到需要的包则会停止搜索，否则继续寻找。找不到则报错
可以在path中添加.pth文件，.pth文件中的路径会被加入到path中，
但是不允许嵌套使用
安装Python时候如果手动设置环境变量，第一个环境变量则是Python.exe
所在路径，这个很好理解，还有一个路径是pip.exe所以在路径，其实pip.exe
路径主要功能是存放第三方程序包所用的资源文件（二进制文件，dll文件），主要为
二进制文件，举个例子假如你要把自己的代码推送到pypi上面供别人使用，
而你代码中依赖一些资源文件，这样安装后你资源文件会放在pip.exe所在目录中，
scripts目录即是此目录。
"""