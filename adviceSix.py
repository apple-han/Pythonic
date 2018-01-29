# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/25 17:08'

###############################
#      编写函数的4个原则        #
#############################

'''
    函数能够带来最大化的代码重用和最小化的代码荣冗余。
    精心设计的函数不仅可以提高代码的健壮性，还可以增加
    可读性，减少维护成本。先来看1-1代码,这段代码到底有
    什么不是之处呢？能否进一步改进呢？怎么才能做到一目
    了然呢？有以下原则
        1，尽量的短小
        2，函数申明应该做到合理
        3，函数的参数设计应该考虑向下兼容
        4，一个函数只做一件事，尽量保证函数粒度的一致性
        5,不要在函数中定义可变对象作为默认值，使用异常
          替换返回错误，保证通过单元测试等等。
    修改之后的代码如1-2所示
    
        
'''

# 1-1
import http.client
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import string

def SendContent(ServerAdr,PagePath,StartLine,EndLine,sender,
                receiver,smtpserver,username,password):
    https = http.client.HTTPSConnection(ServerAdr)
    https.putrequest('Get', PagePath)
    https.putheader('Accept', 'text/html')
    https.putheader('Accept', 'text/plain')
    https.endheaders()
    httpcode, httpmsg, headers = https.getreply()
    if httpcode != 200: assert "Could not get document: Check URL and Path."
    doc = https.getfile()
    data = doc.read()
    doc.close()
    lstr = data.splitlines()
    j=0
    for i in lstr:
        j = j+1
        if i.strip() == StartLine: slice_start=j # find slice start
        elif i.strip() == EndLine: slice_end=j # find slice end
    subject = "Contented get from web"
    msg = MIMEText(string.join(lstr[slice_start:slice_end]),'plain','utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(password, username)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp,quit()

# 1-2
def GetContent(ServerAdr,PagePath):
    https = http.client.HTTPSConnection(ServerAdr)
    https.putrequest('Get', PagePath)
    https.putheader('Accept', 'text/html')
    https.putheader('Accept', 'text/plain')
    https.endheaders()
    httpcode, httpmsg, headers = https.getreply()
    if httpcode != 200: assert "Could not get document: Check URL and Path."
    doc = https.getfile()
    data = doc.read()
    doc.close()
    return data

def ExtractData(inputstring, StartLine, EndLine):
    lstr = inputstring.splitlines()
    j = 0
    for i in lstr:
        j = j + 1
        if i.strip() == StartLine:
            slice_start = j  # find slice start
        elif i.strip() == EndLine:
            slice_end = j  # find slice end
    return lstr[slice_start:slice_end]

def SendEmail(sender,receiver,smtpserver,username,password,content):

    subject = "Contented get from web"
    msg = MIMEText(string.join(content), 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(password, username)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp, quit()
