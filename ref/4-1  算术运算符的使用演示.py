# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 06:54:33 2018
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""
a=20
b=-3
print(a+b)              #加号运算，输出：17
print(a-b)              #减号运算，输出：23
print(a*b)              #乘号运算，输出：-60
print(a/b)              #除号运算，输出：-6.666666666666667
print(a%b)              #取余运算，输出：-1
print(a**b)              #幂运算，输出：0.000125
print(a//b)              #整除运算，输出：-7
print(abs(b))              #绝对值运算，输出：3
print(int("1010",2))              #将字符串以二进制转换成整数，输出：10
print(float("3.14"))              #将字符串换成浮点数，输出：3.14

c =complex(a,b)               #生成复数，输出：(20-3j)
print(c)
print(c.conjugate())              #计算共轭复数，输出：(20+3j)

print(divmod(a, b))              #计算除数与余数，输出：(-7, -1)


