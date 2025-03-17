import os
import time
from json_env import load_env, get_env

start: float = time.time()

# load env from json file
load_env(os.path.join(os.getcwd(),"env.json"))

# log the variables and variable's type
print(get_env("str"), type(get_env("str")))
print(get_env("bool_str"), type(get_env("bool_str")))
print(get_env("int_str"), type(get_env("int_str")))
print(get_env("float_str"), type(get_env("float_str")))
print(get_env("none_str"), type(get_env("none_str")))
print(get_env("none"), type(get_env("none")))
print(get_env("bool"), type(get_env("bool")))
print(get_env("int"), type(get_env("int")))
print(get_env("float"), type(get_env("float")))
print(get_env("array"), type(get_env("array")))
array: list = get_env("array")
for item in array:
    print(type(item))
print(get_env("object"), type(get_env("object")))
json_object: dict = get_env("object")
for key, val in json_object.items():
    print(type(val))
print(f"Test total time cost: {time.time() - start}s")