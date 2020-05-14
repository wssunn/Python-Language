# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:31:43 2018
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""
a=3
b=5
c=None



print(a==b)              	#等于比较，输出：False
print(a!=b)              	#不等于比较，输出：True
print(a>b)              	#大于比较，输出：False
print(a<b)              	#小于比较，输出：True
print(a>=b)              	#大于等于比较，输出：False
print(a<=b)             	#小于等于比较，输出：True
print(a is b)             	#指针等于比较，输出：False
print(a is not b)             	#指针不等于比较，输出：True
print(c is None)             	#None值等于比较，输出：True

c=7
print(a<b<c)              	#链式比较，输出：True


