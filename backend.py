#Backend python tornado

import os
 
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import rabbitmq
import db
import fast_api
 
define("port", default=80, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/post", PostHandler),
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)
 
 
class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.render("frontend.html")

class PostHandler(tornado.web.RequestHandler):
    async def post(self):
        last_name = self.get_argument("last_name", default=None, strip=False)
        name = self.get_argument("first_name", default=None, strip=False)
        patronymic = self.get_argument("patronymic", default=None, strip=False)
        telephone = self.get_argument("telephone", default=None, strip=False)
        message = self.get_argument("message", default=None, strip=False)
        r = last_name+ " " + name + " " + patronymic + " " + str(telephone) + " " + message
        rabbitmq.send(r)

        db.save_in_db(last_name, name, patronymic, telephone, message)
        
        self.render("frontend.html")  
 
 
def main():
    print("Server is working")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
 
 
if __name__ == "__main__":
    main()
    
