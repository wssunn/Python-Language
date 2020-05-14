# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:52:02 2018
@info:《python带我起飞——入门、进阶、商业实战》配套代码
@author: 代码医生 qq群：274962708，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
@ex:推荐阅读《深度学习之TensorFlow入门、原理与进阶实战》
"""

scores = [("Emma",89,90,59),
("Edith",99,49,59),
("Sophia",99,60,20),
("May",40,94,59),
("Ashley",89,90,59),
("Amy",89,90,69),
("Lucy",79,90,59),
("Gloria",85,90,59),
("Abby",89,91,90),]

def handle_filter(a): 
    s = sorted(a[1:])

    #有两科成绩在80分以上，并且一科在60分以下的
    if s[-2]>80 and s[0]<60:
        return True
    #有一科成绩在90分上，并且另外两科成绩都在在60分以下的
    if s[-1]>90 and s[1]<60:
        return True
    #有一科成绩在90分以上，并且三科的平均分在70分以下的
    if s[-2]>80 and sum(s)/len(s)<60:
        return True
    return False


aa = list(filter(handle_filter,scores))
print(aa)
