# !/usr/bin/env python

from copy import deepcopy

def parseError(keypath: [], data) -> []:
    """

    :param key: list ，初始化为空
    :param data: 需要解析的数据
    :return: list, 返回一个数组，每一项都是一个 元组
    """
    res = []
    if not data:
        return res
    if isinstance(data, str):
        res.append((keypath, data))
    if isinstance(data, dict):
        for k, v in data.items():
            _keypath = deepcopy(keypath)
            _keypath.append(k)
            errdata = parseError(_keypath, v)
            res.extend(errdata)
    if isinstance(data, list):
        for index, item in enumerate(data):
            _keypath = deepcopy(keypath)
            index += 1
            _keypath.append("Index#{}".format(index))
            errdata = parseError(_keypath, item)
            res.extend(errdata)
    return res

if __name__ == "__main__" :
    data = {
        "general": {
            "icon": "这个字段为必填项1"
        },
        "roles": [
            None,
            {
                "name": "这个字段不能为空2",
                "label": "这个字段不能为空3"
            }
        ],
        "settings": "这个字段为必填项4"
    }

    results = parseError([], data)
    for path_keys, error_msg in results:
        print("%s => %s" % ('.'.join(path_keys), error_msg))
