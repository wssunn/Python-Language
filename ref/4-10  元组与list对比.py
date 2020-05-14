# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:04:11 2017
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""

#空元素
t=()                                  #空元组
li=[]                                 #空list

#一个元素的注意
t=(3)                                 #一个元素的注意
t1=(3,)                               #必须要加逗号
li=[3]                                #对于list加不加都可以
l1=[3,]                               #对于list加不加都可以
print(t,t1,li,l1)

#元素修改处理
tt='hello'                            #定义一个变量tt
t1 = (1,3,4,tt,3.4,"yes",[1,2],(4,3))   #列表中放置了整型，变量，浮点型，字符串，嵌套列表
print(t1)                             #将其打印出来
t1[6][0]="3445"                       #为元组中的list里面的元素赋值
print(t1)                             #打印内容
t1[0]=3                               #改变元组中的元素，返回错误
