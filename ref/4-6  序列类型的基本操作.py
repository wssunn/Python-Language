# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:13:08 2017

@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""

s='hello'
s2=' daimayisheng'
#连接
print(s+s2)                #输出：hello daimayisheng
#重复
print(s*3)                 #输出：hellohellohello
#检索
print(s[0],s[1],s[2],s[4]) #当索引为正数，方向从左到右，索引从0开始。输出：h e l o
print(s[-1],s[-2],s[-4])   #当索引为负数，方向从右到左，索引从1开始。输出：o l e
print(s[-5] )              #因为是从1开始，所有最后一个是5。输出：h
#print(s[5])               #因为是从0开始，所有最后一个是4。索引5已经超过了字符串的范围，于是报错。输出：IndexError: string index out of range

#反检索
print(s.index('e'))        #返回e在s中的索引，该索引是从左向右的顺序。输出：1
print(s.index('l'))        #当有两个l时，返回第一个。输出：2
#print(s.index('w'))        #因为s中没有w字符。所以报错：ValueError: substring not found
#切片
print(s[1:3])              #从第一个还是到第三个，步长不指定默认为1。输出：    el   
print(s[:3])               #开始位置不指定，默认从第一个字符开始截取,取到第3个。输出： hel
print(s[0:])               #结束位置不指定，默认到最后，即从第一个字符开始截取，一直截取到最后。输出： hello
print(s[:])                #开始与结束都不指定，即从第一个字符开始截取，一直截取到最后。输出： hello
print(s[::2])              #步长为2，即每取一个之后，光标往后移动2个。输出： hlo
print(s[::-2])             #步长为-2，即反方向读取，每取一个之后，光标往前移动2个。输出： olh
print(s[::-1])             #实现字符串的逆序,输出：olleh
print(s[-2::-1])           #实现字符串的逆序,然后再切片输出：lleh
print(s[:0:-1])           #实现字符串的逆序,然后再切片输出：olle
#字符串不能被修改
s[3]='3'                   #TypeError: 'str' object does not support item assignment