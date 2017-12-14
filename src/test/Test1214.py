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

























