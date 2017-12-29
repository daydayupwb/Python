'''
Created on 2017年12月27日

@author: Administrator
'''
from _ast import If
var1 = 'Runoob'
#字符串截取
print(var1[2])
print(var1[1:3])

var2 = "Hello World!"
print("已更新新字符串：", var2[:6] + 'Runoob!')

print('=======格式化字符串=======')
print("我叫 %s 今年 %d 岁！" %('小米', 10))

list = ['google','runoob',1998,2018]
print(list[2])#返回第三个元素
print(list[1:2])#返回从第二个元素开始第三个元素结束，左闭右开的list集合

list[2] = 'hahah'
print(list[2])
del list[3]
print('删除第三个元素: ',list)

dict1 = {'abc':123,'htc':456}
print(dict1['abc'])

dict1['abc'] = 888#更新字典
dict1['ttt'] = 777#添加字典值

print(dict1)

del dict1['abc']#删除字典值
print(dict1)

dict1.clear()#清空字典值
print(dict1)

print('===============Python3 编程第一步===============')
#Python没有switch case语句....
if(1==1):
    print('1')
elif(1==2):
    print('2')
else:
    print('other')

age = int(input("请输入你家狗狗的年龄："))
print('')
if age < 0:
    print('你是在逗我吧！')
elif age == 1:
    print('相当于14岁的人！')
else:
    print('不知道！')

###退出提示
input("点击enter键退出")
































