# _*_ coding:utf-8 _*_
# 爬虫不是先写代码，而是先分析网站
import urllib2
import cookielib
import re   #正则模块

#创建一个cookie对象，来保存cookie
cookie = cookielib.CookieJar()
#urllib2创建cookie得处理器
handler = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener() #构建handler 对象；open可以直接打开网站

def login():
    #登陆请求
    #html = urllib2.urlopen('http://',data='username=&password=').read()
    req = urllib2.Request("http://',data='username=&password=")
    html = opener.open(req).read()
    return html.decode('gb2312')
if u'上东' in login():
    print '登陆成功'
else:
    print '登陆失败'
def getlist():
    req = urllib2.Request('http://')
    req.add_data('xieke=1&shenfen=32')
    html = opener.open(req).read().decode('gb2312')
    reg = ''  #正则
    re.findall(reg,html)