'''
Created on 2018年1月3日

@author: Administrator
'''

print('==============标准库概览==============')
from datetime import date
import doctest
import os, glob, shutil, sys, re, math, random
import re
from urllib.request import urlopen

print(os.getcwd())#获取当前工作目录
#os.system('cmd')#调用系统命令
print(glob.glob('*.py'))#搜索所有py文件
print(sys.argv)

#错误输出
#sys.stderr.write('出错啦。。。。')
#sys.stdin.write("出错啦。。。")
#sys.stdout.write("出错啦。。。")
#sys.exit()

#正则表达式
outstr = re.findall(r'\bf[a-z]*', "which foot or hand fell fastest")
print(outstr)

#数字
print(math.cos(math.pi / 4))

#随机数
print(random.choice(['a','b','c','d']))
print(random.random())

#日期时间
print(date.today())

#数据压缩。。。。
#测试模块
def averge(values):
    return sum(values) / len(values)

print(doctest.testmod())# 自动验证嵌入测试

#单元测试。。。
# import unittest
# class TestStatisticalFunctions(unittest.TestCase):
#     def test_averge(self):
#         self.assertEqual(averge([20,30,56]),40)
# 
# unittest.main()

print("==============正则表达式================")
result = re.match('123', '7123456')#是否在起始位置，是返回，否返回None
#print(result.span())
print(result)
print(re.search('562', '248562'))#不管是否在起始位置

#替换,默认为0 替换所有。
print(re.sub(r'\D', 'h', "1w2f3c4d5e6g", 0))































