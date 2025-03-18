import os
import json
import typing
from types import NoneType
from .keys import key_list
from .types import JsonVar

def json_able(val: typing.Any) -> bool:
    try:
        # 尝试将变量序列化为 JSON
        json.dumps(val)
        return True
    except (TypeError, OverflowError):
        return False

def type_check(val: typing.Any) -> bool:
    if (
        type(val) == int or
        type(val) == float
    ): return True
    elif json_able(val):
        if type(val) == list:
            for i in range(len(val)):
                if type_check(val[i]):
                    continue
                if type(val[i]) == str:
                    val[i] = json.dumps(val[i])
                elif type(val[i]) == bool:
                    if val[i] is True: val[i] = "true"
                    else: val[i] = "false"
                elif type(val[i]) is NoneType: val[i] = "null"
                else: return False
        elif type(val) == dict:
            for key, item in val.items():
                if type_check(item):
                    continue
                elif type(item) == str:
                    val[key] = json.dumps(item)
                elif type(item) == bool:
                    if item is True: val[key] = "true"
                    else: val[key] = "false"
                elif type(item) == NoneType: val[key] = "null"
                else: return False
        return True
    return False


def set_env(key: str, val: JsonVar) -> None:
    if json_able(val):
        if type(val) == str:
            key_list.append(key)
            os.environ[key] = json.dumps(val)
        elif type(val) == bool:
            key_list.append(key)
            if val is True: os.environ[key] = "true"
            else: os.environ[key] = "false"
        elif type(val) is NoneType:
            key_list.append(key)
            os.environ[key] = "null"
        elif type_check(val):
            key_list.append(key)
            os.environ[key] = str(val)
    else: raise TypeError("Unexpected type, .json file can not store it")
