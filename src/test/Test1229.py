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







    

