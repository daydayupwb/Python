'''
Created on 2017年12月7日

@author: Administrator
'''
# 我的第一个python程序
from tkinter.font import BOLD
str1 = "Hello World!"
print(str1)

if True:
    print("is true")
    print(" 出错啦。。。")  # 缩进必须一致，否则会出错
else:
    print("is false")

# 定义变量
_str2 = '123'

strout = "开始" + \
"结尾"
print(strout)

total = ['a', '2', '3',
         'd']

word = "字符串"
sentence = '這是一個句子。'
paragraph = """這是一個段落，
可以由多行組成"""
print(paragraph)
# input("\n\n按下 enter 鍵后退出。")#会自动换行

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

if 1 == 1:
    print('0')
elif True:
    print('1')
else:
    print('其它')

# print默认不换行设置
print(" x", end='')
print(" y", end='')

# 导入其他模块函数
print('\n=======Python import mode=======')
print('遍历数组为：')
for i in total:
    print(i, end=',')

# 遍历字符串
print('\n=======遍历字符串=======')
strArray = 'abcdefg'
for s in strArray:
    print(s, end=',')

# 导入sys模块成员变量
from sys import argv, path
print('\n========python from import=======')
print('path:', path)

print('\n=======调用函数========')
def func01(ss):
    if ss == 1:
        return 1
    else:
        return 0
    
print(func01(2))

print('\n==============基本数据类型=============')
miles = 1000.0000000
print(miles)

print('\n多个变量赋值')
h1=h2=h3=5
a,b,c = 1,2,'runoob'
print(c)

print('\n==============数字=============')
n1,n2,n3,n4 = 20,5.5,True,4+3j
print(type(n4))
print(isinstance(n3, bool))

class A:
    a1 = '2'
class B(A):
    print(A().a1)
    
bol = True
print(bol + 2)

#del bol
#print(bol) #del操作后，bol对象不存在  类似java回收机制？？？

print(2//4)
print(2**3)
print(17%3)
print(4//4)#得到整数必须用双斜杠

str = 'runoob'
print(str[1:])#输出第二到最后的所有字符
print(str[2:5])
print(str*2)#输出字符串两次
print(str + 'Test')
print('\n'*2)
print('11'*2)

print('===================测试转义=====================')
print('Ru\noob')
print(R'Ru\noob')#不会转义

word = 'Python'
print(word[0],word[5])
print(word[-1],word[-6])

print('===================List列表======================')
list = ['abcd', 786, 2.23 , 'runoob', 70.23]
print(list)
tinylist = [123, 'runoob']
print(list[0])#输出第一个元素
print(list[1:3])#输出第二个开始输出到第三个元素
print(list[2:])#输出从第三个元素开始的所有元素
print(tinylist * 2)#输出两次列表
print(list + tinylist)#连接列表

arModify = [1,2,3,4,5,6]
arModify[0] = 10;
arModify[2:5] = [8,8,8]
print(arModify)
arModify[2:5] = [];#将对应元素值设置成空
print(arModify)

print('==================元组===========================')
tuple = ('abcd', 786, 2.23, 'runoob', 70.2 )
tinytuple = (123, 'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

tup = (1,2,3,4,5)
#tup[1] = 33 #不支持修改
tup1 = ()
tup2 = (20,)#不加逗号输出一个元素：20
print(tup1,tup2)

print('=================Set集合====================')
student = {'Tom', 'Jim', 'Mary', 'Tom'}
print(student)#输出集合，重复的元素被自动去掉

print('123')








