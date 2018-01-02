'''
Created on 2018年1月2日

@author: Administrator
'''
from _collections import deque
import sys
from urllib import request


print('===================Python3 函数=======================')

def helloWorld(name,age):#定义函数
    print('age',age)
    return "my name is " + name +',age ' + str(age)

print(helloWorld("wen", 18))#调用函数

#可写函数说明
def printme(str,str2):#str是关键字
    "打印任何传入的字符串"
    print (str)
    return
#调用printme函数
printme(str="菜鸟教程",str2 = '菜鸟教程2')

#不定长参数
def printinfo(arg1, *vartuple):
    print("不定长参数前添加*号")
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return;
#调用不定长参数函数
printinfo(10,29)
printinfo(78,89,39)

print("========================匿名函数========================")
sum = lambda n1,n2:n1 * n2;#lambda 函数的语法只包含一个语句
print(sum(10,20))

print("=======================*****作用域*****=================")
msg= 'bbb'
if True:
    msg = 'aaa'

print(msg)

print("======================global和nonlocal关键字====================")
num = 1
def fun1():
    global num #使用全局变量num
    print(num)
    num = 123
    print(num)
fun1()

def outer():
    num = 10
    def inner():
        nonlocal num # nonlocal关键字说明
        num = 100
        print(num)
    inner()
    print(num)
outer()

print("============================数据结构==========================")
list = [88,99,77,33,44]
list.insert(2, 666)
print(list)
list.append(999)
print(list)
list.reverse()
print(list)
list.remove(77)
print(list)
list.sort(key=None, reverse=False)
print(list)

#列表当做堆栈使用
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()#先进后出 =====堆栈
print(stack)

queue = deque(['jack','rose','machiael'])
queue.appendleft('tom')
print(queue.popleft())#效率低

print('============================列表推导式=========================')
vec1 = [2,4,6]
vec2 = [4,3,9]
nlist = [x*y for x in vec1 for y in vec2]
print(nlist)
hlist = (x*y for x in vec1 for y in vec2)
print(hlist)

print('============================嵌套列表解析=========================')
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
malist = [[row[i] for row in matrix] for i in range(4)]
print(malist)

dictobj = dict([('name','wen'),('age','28'),('location','cd')])
print(dictobj)

print("======遍历技巧======")
knights = {'name':'jack','age':'89','location':'chengdu'}
for k,v in knights.items():
    print(k,v)

for i,v in enumerate(['tic','tac', 'toe']):
    print(i, v)

#同时遍历两个或多个序列
questions = ['name','question','favorite color']
answers = ['lancelot','the holy grail', 'blue']
for q,a in zip(questions,answers):
    print('what is your {0} It is {1}.'.format(q, a))

print("=======Python3 模块========")

for i in sys.argv:
    print(i)

print('路径：' + str(sys.path),'\n')

s = 'Hello Runoob'
print(str(s))
print(repr(s))#多一个单引号

#读写文件
f = open(r"D:\projects\PythonDemo\src\tmp\foo.txt","w")
f.write('good good study,day day up!')
f.close();

r = open(r"D:\projects\PythonDemo\src\tmp\foo.txt","r")
rstr = r.read()
outstr = r.readline()
print(rstr)
print(outstr)
r.close()

response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open(R"D:\projects\PythonDemo\src\tmp\project.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件

print('================类对象=================')
class MyClass:
    '''实例'''
    i = 12345
    def f(self):
        return 'hello world'
#实例化类对象
x = MyClass()#与java区别是不用写new
print(x.i)
print(x.f())

#主类
class People:
    #定义基本属性
    name = ""
    age = 0
    #私有属性
    _weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self._weight = w
    def speak(self):
        print("%s 说： 我 %d 岁 体重 %d 公斤" %(self.name, self.age,self._weight))

#实例化类对象
p = People('张三',29,55)
p.speak()

#单继承
class Student(People):
    location = ''
    def __init__(self,n,a,w,l):
        #调用父类构造函数
        People.__init__(self, n, a, w)
        self.location = l
    #覆盖弗雷的方法
    def speak(self):
        print("%s 说： 我 %d 岁 体重 %d 公斤  家住 %s" %(self.name, self.age,self._weight,self.location))

student = Student('ken',10,60,'四川')
student.speak()#调用子类方法

#多继承
#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(speaker,People):#多继承
    def __init__(self,n,a,w,l):
        People.__init__(self, n, a, w)
        speaker.__init__(self, n, a)
test = sample('tim',25,80,'sichuan')
test.speak()

#重写
class Parent:
    __count = 0 #私有属性
    def myMethod(self):
        print('调用父类的方法')
    def __speak__(self):
        print('我说你是谁啊？ 废话那么多。')
class Child(Parent):
    def myMethod(self):
        print('调用子类的方法')
    def __div__(self):
        print('123')
c = Child()
c.myMethod()
p = Parent()
#print(p.__count)#两个下划线开头为私有属性，只能在内里面调用。
#p.__speak__()#两个下划线开头为私有方法，只能在类里面调用。
c.__div__()



































