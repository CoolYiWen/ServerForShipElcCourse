#历史记录控制器
from Database import Database
import Tools

#获取历史记录
def GetHistory(token):
    datas = Database().GetHistoryByToken(token)
    #不存在记录
    if not datas:
        return {"status": "0", "resp": {}, "error": "There is no history!"}

    histories = []
    for data in datas:
        del data["_id"]
        histories.append(data)

    return {"status": "1", "resp": histories[::-1]}

#清除历史记录
def ClearHistory(token):
    if Database().ClearHistoryByToken(token):
        return {"status": "1", "resp": {}}
    else:
        return {"status": "0", "resp": {}}


