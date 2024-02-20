2024/01/03 
import matplotlib.pyplot as plt
"""设计得非常有意思，绘图时候若没有figure则会创建一个，然后在上面画图。figure为一个画布(窗口)。
若存在figure则在最近活动的画布上画图，当然也有可以指定画布，下面是两个例子。
plt是一个模块，其实也可以当作一个对象(整个模块被设计类似对象，也可以看作单例)
plt就像一个画图室，这个室内管理所有的图以及与画图有关的资源。可以运行下面例子加深理解。
"""
# 创建两个窗口
plt.figure(num=1)
plt.figure(num=2)

# 在第一个窗口中绘制数据
plt.figure(2)
plt.plot([1, 2, 3], [4, 5, 6])

# 在第二个窗口中绘制数据
#plt.figure(1)
plt.plot([1, 2, 3], [7, 8, 9])
plt.figure(1)

#创建一个 Figure 对象。

fig = plt.figure()
#调用 add_subplot() 方法来添加子图，并指定子图在图形中的位置。

ax1 = fig.add_subplot(2, 2, 1)  # 第一行第一列
ax2 = fig.add_subplot(2, 2, 2)  # 第一行第二列
ax3 = fig.add_subplot(2, 2, 3)  # 第二行第一列
ax4 = fig.add_subplot(2, 2, 4)  # 第二行第二列
#这里的参数 (2, 2, 1) 表示将图形分成 2 行 2 列，当前子图位于第一行第一列。

#在每个子图上绘制图形。
ax1.plot([1, 2, 3], [7, 8, 9])
ax2.scatter([1, 2, 3], [7, 8, 9])
ax3.bar([1, 2, 3], [7, 8, 9])
ax4.hist([1, 2, 3], bins=10)

plt.show()