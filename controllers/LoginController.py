#登陆控制器
from Database import Database
import Tools

#登陆
def Login(token):
    result = Database().FindUserByToken(token)
    if result:
        result.pop('token')
        result.pop('_id')
        return {"status":"1",
                "resp":result
                }
    else:
        return {"status":"0",
                "resp":{}
                }

