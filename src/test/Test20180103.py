'''
Created on 2018年1月3日

@author: Administrator
'''

print('==============标准库概览==============')
import os, glob, shutil, sys,re,math,random
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
from datetime import date
print(date.today())

#数据压缩。。。。
#测试模块
def averge(values):
    return sum(values) / len(values)

import doctest
print(doctest.testmod())# 自动验证嵌入测试

#单元测试。。。
# import unittest
# class TestStatisticalFunctions(unittest.TestCase):
#     def test_averge(self):
#         self.assertEqual(averge([20,30,56]),40)
# 
# unittest.main()

























