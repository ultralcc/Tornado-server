#/use/bin/env Python
# coding=utf-8

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.error import Error_Handler
url = [
    (r'/',IndexHandler), 
    (r'/user', UserHandler),
    (r'/.*',Error_Handler),
]
