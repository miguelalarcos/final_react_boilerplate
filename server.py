from tornado import web, ioloop
#import components.fibo
import server.fibo


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

app = web.Application([
    (r"/", MainHandler),
    (r"/main/(.*)", web.StaticFileHandler, {"path": "/home/miguel/development/brython/final"}),
    (r"/components/(.*)", web.StaticFileHandler, {"path": "/home/miguel/development/brython/final/components"}),
    #(r"/fibo/(.*)", web.StaticFileHandler, {"path": "/home/miguel/development/brython/final/components/fibo"}),
    #(r"/app/(.*)", web.StaticFileHandler, {"path": "/home/miguel/development/brython/final/components/main"}),
])


if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()




