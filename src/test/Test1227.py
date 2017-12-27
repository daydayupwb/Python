'''
Created on 2017年12月27日

@author: Administrator
'''
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

