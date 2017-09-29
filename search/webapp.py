#-*- coding:utf8 -*-
import web
urls = {
    '/','Index'
}

class Index:
    def GET(self):
        return 'hello'
if __name__ == '__main__':
    web.application(urls,globals()).run()
