# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:35:08 2017
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""


import pickle                                 #导入pickle模块

tup1 = ('I love Python', [1, 2, 3], None)      #定义一个复杂元素类型的元组 

#测试Python对象与二进制对象互转
p1 = pickle.dumps(tup1)                       #使用pickle模块的dumps将Python对象转成二进制对象
t2 = pickle.loads(p1)                        #使用pickle模块的loads将二进制对象转成Python对象

print(t2)       #将其输出

#测试Python对象与二进制文件互转
path = "a.pkl"
with open(path, 'wb') as f:
    pickle.dump(tup1, f, pickle.HIGHEST_PROTOCOL)#使用pickle模块的dump将Python对象转成二进制对象文件

with open(path, 'rb') as f:
    t3 = pickle.load(f) #使用pickle模块的load将二进制对象文件转成Python对象
    print(t3)                   #将其输出
    
