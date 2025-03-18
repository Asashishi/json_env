import os
import json
from types import NoneType

from .types import JsonVar
from .keys import key_list

def get_formated_environ_var(key: str) -> str:
    val: JsonVar = os.environ.get(key)
    if type(val) == NoneType: val = "null"
    return (
        val.
        replace("'",'"').
        replace("None", "null").
        replace("True","true").
        replace("False","false")
    ).replace("'",'"')

def get_env(key: str) -> JsonVar:
    json_var: JsonVar = json.loads(get_formated_environ_var(key))
    if type(json_var) == list:
        for i in range(len(json_var)):
            if type(json_var[i]) == str: json_var[i] = json.dumps(json_var[i]).replace('"', '')
    elif type(json_var) == dict:
        for key, val in json_var.items():
            if type(val) == str: json_var[key] = json.dumps(val).replace('"','')
    return json_var

def show_all() -> None:
    for key in key_list:
        val: JsonVar = get_env(key)
        print(f"key: {key}, val: {val}, type: {type(val)}")