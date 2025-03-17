# Introduce json_env
- This pak opened base on MIT Licence
- This is a simple environment variable solution for .json file
- It's based on 'os' and 'json' libs
- Use this lib you don't need to worry type issue of 'os.environ' it's all handled by this pak

# Install
```shell
pip install json-env-sln==1.0.7
```
# Example
## Use case
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
## How to use
```python
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
Test total time cost: 0.001172780990600586s
```



