# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:14:14 2017
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""

tt='hello'
list1 = [1,4,tt,3.4,"yes",[1,2]]   #定义一个涵盖各种类型的list
print(list1,id(list1))               #将其内容及地址打印出来[1, 4, 'hello', 3.4, 'yes', [1, 2]] 151672328


#比较list中添加元素的几种方法的区别
list3 = [6,7]                        #定义list3作为后面拼接实验使用
l2 = list1+list3                     #使用+将list1与list3连接一起，得到l2
print(l2,id(l2))                     #输出l2的内容及地址[1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7] 151650568

l2=list1.extend(list3)               #使用extend将list1与list3连接一起，给到l2
print(l2,id(l2))                     #输出l2的内容及地址None 1722913824
print(list1,id(list1))               #将list1内容及地址打印出来[1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7] 151672328

l2=list1.append(list3)               #使用append将list3加入到list1中，给到l2
print(l2,id(l2))                     #输出l2的内容及地址None 1722913824
print(list1,id(list1))               #将list1内容及地址打印出来[1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7, [6, 7]] 151672328


#删除操作
print(list1)                         #输出list1的内容及地址[1, 4, 'hello', 3.4, 'yes', [1, 2], 6, 7, [6, 7]]
del list1[2:5]                       #删除list1的切片
print(list1)                         #再次输出list1的内容及地址 [1, 4, [1, 2], 6, 7, [6, 7]]
del list1[2]                         #删除list1的索引
print(list1)                         #再次输出list1的内容及地址 [1, 4, 6, 7, [6, 7]]

l2=list1
print(id(l2),id(list1))              #打印地址
del list1                            #删除list1变量
print(l2)                            #l2还能访问，表明地址指向的数据并没有删
#print(list1)                         #再次输出list1的内容及地址 NameError: name 'list1' is not defined

l3=l2
del l2[:]                         #删除l2全部内容
print(l2)                         #输出l2的内容及地址 []
print(l3)                         ##输出l3的内容及地址也为 []，表明数据已经被删             
