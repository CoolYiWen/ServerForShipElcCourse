#程序入口
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import Handlers

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/course/login", Handlers.LoginHandler),
                    (r"/course/check", Handlers.CheckHandler),
                    (r"/course/collect", Handlers.CollectHandler),
                    (r"/course/collection", Handlers.CollectionHandler),
                    (r"/course/history/get/(\w+)", Handlers.HistoryHandler),
                    (r"/course/history/clear", Handlers.ClearHistoryHandler),
                    ]

        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()