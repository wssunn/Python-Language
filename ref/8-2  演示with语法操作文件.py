# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:30:18 2017

@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""

with open('a.txt','wb+') as f:          #以二进制的方式打开一个文件
    try:	
        f.write('I like Python!')   		#以文本的方式写入一个用二进制打开的文件，会报错  
    except Exception as e: 			#将错误异常捕获
        print(e )
        f.write(b'I like Python!')  		#以bytes对象的形式进行读写


with open('a.txt','r+') as f: #打开文件				
    for line in f:						#直接使用for循环读取文件
        print(line)					#将内容打印出来


