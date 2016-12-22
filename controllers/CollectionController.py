#收藏控制器
from Database import Database
import Tools

#收藏设备
def Collect(checkId, cover):
    data = Database().FindCheckDataByCheckId(checkId)
    #存在验算结果
    if data:
        name = data["name"]
        collection = Database().FindCollectionByName(name)
        #若数据库中已收藏
        if collection:
            #覆盖记录
            if "1" == cover:
                data["_id"] = collection["_id"]
                if Database().UpdateCollection(data):
                    return {"status":"1", "resp":{"exist":"1"}}
            #提示客户端是否覆盖
            else:
                return {"status":"0", "resp":{"exist":"1"}}
        #数据库中未收藏
        else:
            if Database().InsertCollection(data):
                return {"status":"1", "resp":{"exist":"0"}}
    #不存在验算结果，收藏无效
    else:
        return {"status":"0", "resp":{}, "error":"No check in memory"}

#获取收藏的设备
def GetCollections():
    datas = Database().GetAllCollections()
    #数据库中无记录
    if not datas:
        return {"status":"0", "resp":{}, "error":"There is no one collection!"}
    #返回收藏记录
    collections = []
    for data in datas:
        data.pop('_id')
        collections.append(data)

    return {"status":"1", "resp":collections}

#删除收藏的记录
def RemoveCollection(name):
    if Database().RemoveCollectionByName(name):
        return {"status":"1", "resp":{}}
    else:
        return {"status":"0", "resp":{}}

