'''
Created on 2017年12月14日

@author: Administrator
'''
print('=================Set集合====================')
student = {'Tom', 'Jim', 'Mary', 'Tom'}
print(student)#输出集合，重复的元素被自动去掉

#成员测试
if('Jim' in student):
    print('Jim 在集合中。。。')

#set集合运算
a = set('abracadabra')# abcdr
b = set('alacazam')# aclmz
print(a)
print(a - b)#a和b的差集
print(a | b)#a和b的并集
print(a & b)#a和b的交集
print(a ^ b)#a和b中不同时存在的元素

