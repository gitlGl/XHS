#2024/02/19
from decimal import Decimal, localcontext, ROUND_HALF_UP,getcontext
a = 4.2 + 2.1
print(a,a == 6.3)#输出：6.300000000000001 False

a ,b= Decimal('4.2') ,Decimal('2.1')
print(a + b ,a + b == Decimal('6.3'))#输出：6.3 True

nums = [1.23e+18, 1, -1.23e+18]#sum计算过程因为精度问题“1”被舍弃
sum(nums) # 0.0

import math#应该math中的sum函数修复精度问题
math.fsum(nums)#1.0

# 获取当前默认上下文， 查看默认精度
default_context = getcontext()
default_precision,rounding = default_context.prec,default_context.rounding
print(default_precision,rounding)  # 输出: 28 ROUND_HALF_EVEN

# 修改默认保留位数
default_context.prec = 3
num = Decimal('1.225')
print(num.quantize(Decimal('0.00')))#输出: 1.22
print(Decimal('1.235') - Decimal('0.01'))#默认为银行家舍入ROUND_HALF_EVEN,# 输出: 1.22

# 使用上下文管理器结合设置精度和舍入模式
with localcontext() as ctx:
    ctx.prec = 3  # 设置上下文中的保留位数
    ctx.rounding = ROUND_HALF_UP  # 设置上下文中的舍入模式为四舍五入。
    print(num.quantize(Decimal('0.00')))  # 对num进行舍入并保留两位小数,输出: 1.23
    print(Decimal('1.235') - Decimal('0.01'))# 输出: 1.23
    """
ROUND_HALF_EVEN，
        银行家舍入规则：如果要舍弃的数字小于5，则直接舍弃。如果要舍弃的数字大于5，则进行进位。
        如果要舍弃的数字等于5，且前一位数字为偶数，则直接舍弃；如果前一位数字为奇数，则进行进位 
ROUND_HALF_UP 
    四舍五入
    """
print(Decimal('1.235') - Decimal('0.01'))# 输出: 1.22