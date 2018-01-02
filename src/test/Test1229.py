'''
Created on 2017年12月29日

@author: Administrator
'''
print('=====================Python3 循环语句=======================')
#while 循环,Python没有do...while循环。
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1

print('1 到 %d 之和为：%d' %(n,sum))

#无限循环：服务器上客户端的实时请求非常有用
#var = 1
#while var == 1:
    #print('123')

#while 循环使用else语句
count = 0
while count < 5:
    print(count, " 小于5")#只有一条语句，可以将该语句与while写在同一行中
    count = count + 1
else:
    print(count, " 大于或等于5")

#for循环
sites = ['baidu', 'google', 'runoob', 'taobao']
for site in sites:
    if site == 'runoob':
        print('菜鸟教程')
        break#跳出循环体
    print('循环数据 ' + site)
else:
    print("没有循环数据")
print('完成循环！')
#遍历数字序列
for i in range(5):
    print(i)# 0 1 2 3 4 
print('========for========')
for j in range(5, 9, 2):
    print(j)
#创建list
list = list(range(5))
print(list)

pass#空语句

print('==============Python3 迭代器与生成器============')
import sys #引入sys模块
ilist = [1,2,3,4]
it = iter(ilist)
print(next(it))

iter22 = [3,4,5,6]
print(next(iter(iter22)))

for x in iter(iter22):
    print(x,end=',')

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

def fibonacci(n):#生成器函数
    a,b,counter = 0,1,0
    while True:
        if(counter > n):
            return
        yield a#使用yield的函数被称为生成器
        a,b = b,a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
