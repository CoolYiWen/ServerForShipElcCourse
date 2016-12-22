#处理程序
import tornado.web
from tornado.escape import json_decode
import json

from controllers.CollectionController import Collect, GetCollections, RemoveCollection
from controllers.HistoryController import GetHistory, ClearHistory
from controllers.LoginController import Login
from controllers.CheckController import Check

#登录处理
class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        token = self.get_argument("token")
        result = Login(token)
        self.write(json.dumps(result))

#验算处理
class CheckHandler(tornado.web.RequestHandler):
    def post(self):
        token = self.get_argument("token")
        data = json_decode(self.get_argument("data"))
        result = Check(token, data)
        self.write(json.dumps(result))

#收藏处理
class CollectHandler(tornado.web.RequestHandler):
    def post(self):
        checkId = self.get_argument("checkId")
        cover = self.get_argument("cover")
        result = Collect(checkId, cover)
        self.write(json.dumps(result))

#收藏项处理
class CollectionHandler(tornado.web.RequestHandler):
    def get(self):
        result = GetCollections()
        self.write(json.dumps(result))

    def post(self):
        name = self.get_argument("name")
        result = RemoveCollection(name)
        self.write(json.dumps(result))

#历史记录获取处理
class HistoryHandler(tornado.web.RequestHandler):
    def get(self, token):
        result = GetHistory(token)
        self.write(json.dumps(result))

#历史清除记录处理
class ClearHistoryHandler(tornado.web.RequestHandler):
    def post(self):
        token = self.get_argument("token")
        result = ClearHistory(token)
        self.write(json.dumps(result))
