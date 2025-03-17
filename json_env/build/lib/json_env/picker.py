import os
import json
from .type import JsonVar

def get_formated_environ_var(key: str) -> str:
    return (
        os.environ.get(key).
        replace("'",'"').
        replace("None", "null").
        replace("True","true").
        replace("False","false")
    ).replace("'",'"')

def get_env(key: str) -> JsonVar:
    json_var: JsonVar = json.loads(get_formated_environ_var(key))
    if isinstance(json_var, dict):
        for key, val in json_var.items():
            if isinstance(val, str): json_var[key] = json.dumps(val).replace('"','')
    elif isinstance(json_var, list):
        for i in range(len(json_var)):
            if isinstance(json_var[i], str): json_var[i] = json.dumps(json_var[i]).replace('"','')
    return json_var