#-*-coding:utf-8-*-
import web
#路由定义
urls = (
    '/','Index' #index 是一个类，这个类必须存在
)

render = web.template.render('templates') #实力还模板文件对象
#db = web.database(dbn='mysql',host='127.0.0.1',port='3306',user='root',pw='123456',db='4399',charset='utf8')
class Index(object):
    # 定义方法，不能以数字开头, 函数名是用户请求的方式
   def GET(self):
        #data = db.query('select * from games where 1=1') #执行sql语句
        #print data
        #for i in data:
        #    print i
        return render.index()

if __name__=='__main__':
    web.application(urls,globals()).run()