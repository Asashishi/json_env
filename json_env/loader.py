import os
import json
from .types import JsonVar
from .keys import key_list

def load_env(env_path: str) -> None:
    try:
        with open(env_path, 'r') as env_file:
            data: dict[str, JsonVar] = json.load(env_file)
        for key, val in data.items():
            key_list.append(key)
            if type(val) == str:
                os.environ[key] = json.dumps(val)
                continue
            os.environ[key] = str(val)
    except Exception as error: raise error
