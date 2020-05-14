# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 07:55:03 2018
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""


#模块函数被覆盖
from getenv import *  
def showENV():
    print("this is my env")
showENV()  

#本地函数被覆盖 
def showENV():
    print("this is my env") 
from getenv import *    
showENV()
