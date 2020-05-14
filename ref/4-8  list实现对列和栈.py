# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:28:46 2017

@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""
#list 实现队列，先进先出
queue = []                      #定义一个空list，当作队列
queue.insert(0,1)               #向队列里放入一个整型元素 1
queue.insert(0,2)               #向队列里放入一个整型元素 2
queue.insert(0,"hello")         #向队列里放入一个字符型元素 hello
print("取第一个元素",queue.pop()) #从队列里取一个元素，根据先进先出原则，输出 1
print("取第二个元素",queue.pop()) #从队列里取一个元素，根据先进先出原则，输出 2
print("取第三个元素",queue.pop()) #从队列里取一个元素，根据先进先出原则，输出 hello

#list 实现栈，先进后出
stack = []                     #定义一个空list，当作栈
stack.append(1)                #向栈里放入一个整型元素 1
stack.append(2)                #向栈里放入一个整型元素 2
stack.append("hello")          #向栈里放入一个字符型元素 hello
print("取第一个元素",stack.pop())#从栈里取一个元素，根据后进先出原则，输出 hello
print("取第二个元素",stack.pop())#从栈里取一个元素，根据后进先出原则，输出 2
print("取第三个元素",stack.pop())#从栈里取一个元素，根据后进先出原则，输出 1



from collections import deque  
queueandstack  = deque()                #创建空结体构，既可以当队列又可以当栈  

queueandstack.append(1)                #向空结体里放入一个整型元素 1 
queueandstack.append(2)                #向空结体里放入一个整型元素 2 
queueandstack.append("hello")         #向空结体里放入一个字符型元素 hello
print(list(queueandstack))
  
print(queueandstack.popleft())       #从队列里取一个元素，根据先进先出原则，输出 1
print(queueandstack.pop())           #从栈里取一个元素，根据后进先出原则，输出 hello
print('Now queue is', list(queueandstack))  
  

