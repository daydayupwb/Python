'''
Created on 2017年12月14日

@author: Administrator
'''
from _ast import If
from symbol import if_stmt
from math import ceil, floor
print('=================Set集合====================')
student = {'Tom', 'Jim', 'Mary', 'Tom'}
print(student)#输出集合，重复的元素被自动去掉

#成员测试
if('Jim' in student):
    print('Jim 在集合中。。。。。')

#set集合运算
a = set('abracadabra')# abcdr
b = set('alacazam')# aclmz
print(a)
print(a - b)#a和b的差集
print(a | b)#a和b的并集
print(a & b)#a和b的交集
print(a ^ b)#a和b中不同时存在的元素

print('=================Dictionary==================')
dict = {}#空字典
dict['one'] = '菜鸟'
dict[2] = '菜鸟2'
print(dict['one'])
print(dict[2])
tinydict = {'name':'runoob', 'code':1, 'site':'www.123.com'}
print(tinydict.keys());#输出所有key值
print(tinydict.values())#输出所有value值
cpy = tinydict.copy()#复制字典
print(cpy)
cpy.clear()#清空字典
print(cpy)
print(tinydict.get('name'))#根据key获取值

print('==================Python3 解释器==================')
'''
注释1
注释2
'''

#注释2
"""
我的注释
我的注释
"""
print('==================Python3 逻辑运算符==================')

x = False
print(not x)

list = [1,2,3,4,5]
listele = 10
if(listele in list):
    print('在包含之中。。。')
else:
    print('不在包含之中。。。')

copylist = list
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
print(copylist == list)
print(copylist is list[:])

intavalue = 3.0
print(int(intavalue))#转换成整数
print(2**4)

print('=================Python3 成员运算符====================')
a = 10
b = 8
alllist = [1,2,3,10,20]
if(a in alllist):
    print('a 在alllist 中。。。')
else:
    print('a 不在alllist 中。。。')
if(b not in alllist):
    print('b 不在alllist 中。。。')
else:
    print('b 在alllist 中。。。')

print('================Python3 身份运算符=====================')
s1 = 20
s2 = 20
print(s1 is s2)
print(s1 is not s2)

print('================Python3 数字==========================')
var1 = 1
var2 = 10
print(var1)
#del var1
print(var1)

print('================数学函数=======================')
print(abs(-100))
print(ceil(4.1))
print(floor(5.9))














