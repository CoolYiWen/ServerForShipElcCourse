#从数据库中读取数据和保存数据

import pymongo

#实现单列模式
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

#数据库
class Database(Singleton):
    #验证列表
    checkList = []
    checkId = int(0)

    def __init__(self):
        # 链接数据库服务器
        client = pymongo.MongoClient("localhost", 27017)
        db = client.course
        self.db = db
        # 添加对数据库的集合变量
        self.users = db.users
        self.collections = db.collections

    #查找用户
    def FindUserByToken(self, token):
        user = self.users.find_one({"token":token})
        return user

    #添加验算项
    def InsertCheckData(self, data):
        self.checkId += 1
        self.checkList.append({"checkId":self.checkId, "data":data})

        if self.checkId == 50:
            self.checkId = 0

        if len(self.checkList) == 50:
            i = 0
            while(i < 25):
                self.checkList.pop(0)
                i += 1

        return self.checkId

    #查找验算项
    def FindCheckDataByCheckId(self, checkId):
        for i in range(len(self.checkList)):
            if int(checkId) == self.checkList[i]["checkId"]:
                print("get")
                return self.checkList[i]["data"]
        return None

    #添加收藏项
    def InsertCollection(self, data):
        ObjectId = self.collections.insert_one(data)
        return ObjectId

    #查找收藏项
    def FindCollectionByName(self, name):
        collection = self.collections.find_one({"name":name})
        return collection

    #更新收藏项
    def UpdateCollection(self, data):
        ObjectId = self.collections.save(data)
        return ObjectId

    #获取所有收藏设备
    def GetAllCollections(self):
        collections = self.collections.find()
        return collections

    #删除收藏的设备
    def RemoveCollectionByName(self, name):
        collection = self.collections.find_one({"name":name})
        ObjectId = self.collections.delete_one(collection)
        return ObjectId

    #添加历史记录
    def InsertHistoryByToken(self, token, data):
        ObjectId = self.db[token].insert_one(data)
        return ObjectId

    #获取历史记录
    def GetHistoryByToken(self, token):
        histories = self.db[token].find()
        return histories

    #清空历史记录
    def ClearHistoryByToken(self, token):
        result = self.db[token].delete_many({})
        return result