# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:24:32 2017

@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""
#在范围[-5, 256]之间的小整数
int1=-5
int2=-5
print("[-5, 256]情况下的两个变量指针",id(int1),id(int2))

#对于字符串
s1="3344"
s2= "3344"
print("字符串情况下的两个变量指针",id(s1),id(s2))

#大于256的整数
int3=257
int4=257
print("大于256的整数情况下的两个变量指针",id(int3),id(int4))

#大于0的浮点数
f1=256.4
f2=256.4
print("大于0的浮点数情况下的两个变量指针",id(f1),id(f2))

#小于0的浮点数
f1=-2.45
f2=-2.45
print("小于0的浮点数情况下的两个变量指针",id(f1),id(f2))

#小于-5的整数
n1=-6
n2=-6
print("小于-5的整数情况下的两个变量指针",id(n1),id(n2))

def fun():
    #[-5,256]
    int1=-5
    print("fun中-5的指针",id(int1),id(int2))
    
    #字符串类型
    s1="3344"
    print("fun中3344字符串的指针",id(s1),id(s2))
    
    #>256
    int3=257
    print("fun中257的指针",id(int3),id(int4))
    
    #浮点类型
    f1=256.4
    print("fun中256.4的指针",id(f1),id(f2))  
    
    #<-5
    n1=-6
    print("fun中-6的指针",id(n1),id(n2))
    
fun()

