#计算输入类

class Input(object):
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.num = data["num"]
        self.pmax = data["pmax"]
        self.p1 = data["p1"]
        self.e = data["e"]
        self.k21 = data["k21"]
        self.k01 = data["k01"]
        self.k22 = data["k22"]
        self.k02 = data["k02"]
        self.k23 = data["k23"]
        self.k03 = data["k03"]
        self.k24 = data["k24"]
        self.k04 = data["k04"]
        self.type1 = data["type1"]
        self.type2 = data["type2"]
        self.type3 = data["type3"]
        self.type4 = data["type4"]