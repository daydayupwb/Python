'''
Created on 2018年1月11日

@author: Administrator
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@abc.com'
receivers = ['888888@qq.com']#接收邮件地址
message = MIMEText('Python 邮件发送测试。。。', 'plain', 'utf-8')
message['From'] = Header('菜鸟教程','utf-8')
message['To'] = Header('测试','utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpobj = smtplib.SMTP('localhost')#由于没有配置smtp服务器，会导致发送失败。
    smtpobj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print("Error: 无法发送邮件!")



