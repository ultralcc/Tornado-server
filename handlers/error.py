import tornado.web

class Error_Handler(tornado.web.RequestHandler):

    def get(self):
        self.set_status(404)
        self.render('404page.html')
