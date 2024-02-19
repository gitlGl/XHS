#2023/11/11#序列化保存对象
import dlib,pickle
import numpy as np
from dlib import vector
from dlib import array as dlib_array
from numpy import array

x = np.arange(10)
y = x ** 2
np.savez("x_y-squared.npz", x_axis=x, y_axis=y)#保存为二进制文本

load_xy = np.load("x_y-squared.npz")
print(load_xy.files)#['x_axis', 'y_axis']
x = load_xy["x_axis"]
y = load_xy["y_axis"]

dlib_array1 = dlib_array([1, 2, 3])
print(type(dlib_array1))#<class 'dlib.dlib.array'>

dlib_v1 = vector(dlib_array1)
print(type(dlib_v1))#<class 'dlib.dlib.vector'>

str_vector = dlib_v1.__repr__()#文本形式保存
#输出：dlib.vector([1, 2, 3]) <class 'dlib.dlib.vector'>
print(str_vector,type(eval(str_vector)))

np_array = np.array([1,3,4])
str_np_array = np_array.__repr__()

np_array2 = eval(str_np_array)
print(type(np_array2))#<class 'numpy.ndarray'>

#序列化后以二进制形式保存
pick = pickle.dumps(np_array)
print(type(pick))