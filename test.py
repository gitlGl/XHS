#以前进行文件目录操作时候经常使用os.walk函数
#glob其实更好用与直接,还有新出的pathlib库中的glob
#编程的门槛总体上是 越来越低了
import glob,os,pathlib

# 匹配当前目录及其所有子目录中的所有文本文件
files = glob.glob('**/*.txt', recursive=True)

# 匹配当前目录下以 'data_' 开头的所有文件
data_files = glob.glob('data_*.txt')

 #匹配 'myfolder' 文件夹中的所有图片文件
image_files = glob.glob('myfolder/*.{jpg,png,gif}', recursive=True)

# 匹配当前目录下的所有文本文件并获取绝对路径
txt_files = glob.glob('*.txt')
absolute_paths = [os.path.abspath(f) for f in txt_files]
