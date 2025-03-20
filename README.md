# Introduce
- This pak opened base on MIT Licence
- This is a simple environment variable solution for .json file
- It's based on 'os' and 'json' libs
- Use this lib you don't need to worry type issue of 'os.environ' it's all handled by this pak

# What's new 1.1.3
- You can set environment variables now!
```python
set_env(key: str, val: JsonVar | Any)
```
- You can show all environment variables now!
```python
show_all()
```
# What's new 1.1.9
- Improve performance

# Install
```shell
pip install json-env-sln
```
# Example
## test json file
```json
{
  "str": "Asashishi",
  "bool_str": "true",
  "int_str": "107",
  "float_str": "1.07",
  "none_str": "null",
  "none": null,
  "bool": false,
  "int": 107,
  "float": 1.07,
  "array": [
    "Asashishi",
    "true",
    "107",
    "1.07",
    "null",
    null,
    false,
    107,
    1.07
  ],
  "object": {
    "str": "Asashishi",
    "bool_str": "true",
    "int_str": "107",
    "float_str": "1.07",
    "none_str": "null",
    "none": null,
    "bool": false,
    "int": 107,
    "float": 1.07,
    "array": [
      "Asashishi",
      "true",
      "107",
      "1.07",
      "null",
      null,
      false,
      107,
      1.07
    ]
  }
}
```
## Use
### Test case
```python
import os
import time
from json_env import set_env, get_env, load_env, show_all

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

print("="*120)
print("="*120)

set_env("set_str", get_env("str"))
print(get_env("set_str"), type(get_env("set_str")))
set_env("set_bool_str", "true")
print(get_env("set_bool_str"), type(get_env("set_bool_str")))
set_env("set_int_str","107")
print(get_env("set_int_str"), type(get_env("set_int_str")))
set_env("set_float_str","1.07")
print(get_env("set_float_str"), type(get_env("set_float_str")))
set_env("set_none_str","null")
print(get_env("set_none_str"), type(get_env("set_none_str")))

set_env("set_none",None)
print(get_env("set_none"), type(get_env("set_none")))
set_env("set_bool",True)
print(get_env("set_bool"), type(get_env("set_bool")))
set_env("set_int",107)
print(get_env("set_int"), type(get_env("set_int")))
set_env("set_float",1.07)
print(get_env("set_float"), type(get_env("set_float")))

set_env("set_array", array)
print(get_env("set_array"), type(get_env("set_array")))
set_array: list = get_env("set_array")
for item in set_array:
    print(type(item))

set_env("set_object", json_object)
print(get_env("set_object"), type(get_env("set_object")))
set_json_object: dict = get_env("set_object")
for key, val in set_json_object.items():
    print(type(val))

print("="*120)
print("="*120)

# show all
show_all()

print(f"Test total time cost: {time.time() - start}s")
```
## The results are
```text
Asashishi <class 'str'>
true <class 'str'>
107 <class 'str'>
1.07 <class 'str'>
null <class 'str'>
None <class 'NoneType'>
False <class 'bool'>
107 <class 'int'>
1.07 <class 'float'>
['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07] <class 'list'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'NoneType'>
<class 'bool'>
<class 'int'>
<class 'float'>
{'str': 'Asashishi', 'bool_str': 'true', 'int_str': '107', 'float_str': '1.07', 'none_str': 'null', 'none': None, 'bool': False, 'int': 107, 'float': 1.07, 'array': ['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07]} <class 'dict'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'NoneType'>
<class 'bool'>
<class 'int'>
<class 'float'>
<class 'list'>
================================================================================================================================================================================================================================================
================================================================================================================================================================================================================================================
Asashishi <class 'str'>
true <class 'str'>
107 <class 'str'>
1.07 <class 'str'>
null <class 'str'>
None <class 'NoneType'>
True <class 'bool'>
107 <class 'int'>
1.07 <class 'float'>
['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07] <class 'list'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'NoneType'>
<class 'bool'>
<class 'int'>
<class 'float'>
{'str': 'Asashishi', 'bool_str': 'true', 'int_str': '107', 'float_str': '1.07', 'none_str': 'null', 'none': None, 'bool': False, 'int': 107, 'float': 1.07, 'array': ['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07]} <class 'dict'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'NoneType'>
<class 'bool'>
<class 'int'>
<class 'float'>
<class 'list'>
================================================================================================================================================================================================================================================
================================================================================================================================================================================================================================================
key: str, val: Asashishi, type: <class 'str'>
key: bool_str, val: true, type: <class 'str'>
key: int_str, val: 107, type: <class 'str'>
key: float_str, val: 1.07, type: <class 'str'>
key: none_str, val: null, type: <class 'str'>
key: none, val: None, type: <class 'NoneType'>
key: bool, val: False, type: <class 'bool'>
key: int, val: 107, type: <class 'int'>
key: float, val: 1.07, type: <class 'float'>
key: array, val: ['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07], type: <class 'list'>
key: object, val: {'str': 'Asashishi', 'bool_str': 'true', 'int_str': '107', 'float_str': '1.07', 'none_str': 'null', 'none': None, 'bool': False, 'int': 107, 'float': 1.07, 'array': ['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07]}, type: <class 'dict'>
key: set_str, val: Asashishi, type: <class 'str'>
key: set_bool_str, val: true, type: <class 'str'>
key: set_int_str, val: 107, type: <class 'str'>
key: set_float_str, val: 1.07, type: <class 'str'>
key: set_none_str, val: null, type: <class 'str'>
key: set_none, val: None, type: <class 'NoneType'>
key: set_bool, val: True, type: <class 'bool'>
key: set_int, val: 107, type: <class 'int'>
key: set_float, val: 1.07, type: <class 'float'>
key: set_array, val: ['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07], type: <class 'list'>
key: set_object, val: {'str': 'Asashishi', 'bool_str': 'true', 'int_str': '107', 'float_str': '1.07', 'none_str': 'null', 'none': None, 'bool': False, 'int': 107, 'float': 1.07, 'array': ['Asashishi', 'true', '107', '1.07', 'null', None, False, 107, 1.07]}, type: <class 'dict'>

Test total time cost: 0.0015146732330322266s
```
