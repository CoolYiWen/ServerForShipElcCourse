#把Object对象转换成Dict对象
def convert_to_dict(obj):
  dict = {}
  dict.update(obj.__dict__)
  return dict

#把对象列表转换为字典列表
def convert_to_dicts(objs):
  obj_arr = []
  for o in objs:
    #把Object对象转换成Dict对象
    dict = {}
    dict.update(o.__dict__)
    obj_arr.append(dict)
  return obj_arr