import os
import json
from types import NoneType

from .types import JsonVar
from .keys import key_list

def get_formated_environ_var(key: str) -> str:
    val: JsonVar = os.environ.get(key)
    if type(val) == NoneType: return  "null"
    return (
        val.
        replace("'",'"').
        replace("None", "null").
        replace("True","true").
        replace("False","false")
    ).replace("'",'"')

def get_env(key: str) -> JsonVar:
    return json.loads(get_formated_environ_var(key))

def show_all() -> None:
    for key in key_list:
        val: JsonVar = get_env(key)
        print(f"key: {key}, val: {val}, type: {type(val)}")