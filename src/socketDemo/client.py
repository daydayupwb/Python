'''
Created on 2018年1月11日
客户端
@author: Administrator
'''
import socket

#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()

#设置端口号
port = 9999

#连接服务器，指定主机和端口
s.connect((host, port))

#接收小于1024字节的数据
msg = s.recv(1024)
s.close()

print(msg.decode('utf-8'))

