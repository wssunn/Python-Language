# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 08:15:58 2018
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""



import model3.getenv as getenv	 				#导入自定义模块getenv 

def showENV():					#实现同名函数showENV
    print("this is my env")
    
showENV()						#调用本地函数
getenv.showENV()				#调用getenv模块里的函数
