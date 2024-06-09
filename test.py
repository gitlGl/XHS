import numpy as np  
import math  

# 设定x的范围和分割数（更精细的分割将得到更精确的结果）  
x_start = 0  
x_end = 2 * math.pi  
num_rectangles = 1000  # 你可以调整这个数来改变矩形数量  
  
# 计算每个矩形的宽度  
delta_x = (x_end - x_start) / num_rectangles  
  
# 计算每个矩形的高度（对应y=sin(x)的值）  #注意这里加1是为了包含端点  
x_values = np.linspace(x_start, x_end, num_rectangles+1)
y_values = np.sin(x_values)  
#使用绝对值来确保我们考虑函数与x轴的正负两侧  
heights = np.abs(y_values[:-1])
  
# 计算每个矩形的面积并求和  
rectangle_areas = heights * delta_x  
total_area = np.sum(rectangle_areas)  
  
# 输出结果  
print(total_area)
