import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application
from tornado.options import define, options

define("port", default = 80, help = "run on given port", type = int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print("Development server is running at http://49.159.109.97:",options.port)
    print("Quit the server with Ctrl-C")
    
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
   main()
