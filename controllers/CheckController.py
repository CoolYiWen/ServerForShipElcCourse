#验证控制器

from beans.Entity import Entity
from beans.Output import Output
from Database import Database
import Algorithm
import Tools

def Check(token, data):
    #提取数据并转化成对象
    entity = Entity(data)
    outputFromClient = Output(data)
    #运算
    output = Algorithm.NeedCoefficientMethod(data, entity)
    #对象转化为字典
    outputFromClientDict = Tools.convert_to_dict(outputFromClient)
    outputDict = Tools.convert_to_dict(output)
    entityDict = Tools.convert_to_dict(entity)
    #验证成功
    if CheckOutput(outputFromClientDict, outputDict):
        #内存中保存本次验算记录
        checkId = Database().InsertCheckData(entityDict)
        #添加到历史记录
        Database().InsertHistoryByToken(token, data)

        result = {"status":"1",
                  "resp":{
                      "checkId":checkId}
                  }
    #验算失败
    else:
        result = {"status": "0",
                  "resp": {}
                  }

    return result

#判断输出结果是否相同
def CheckOutput(dict1, dict2):
    result = True
    for key in dict1:
        if type(dict1[key]) == "bool":
            if dict1[key] != dict2[key]:
                result = False
        else:
            if (dict1[key] - dict2[key]) > 0.001:
                result = False
    return result

