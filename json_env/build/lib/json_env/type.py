import typing

JsonSimpleVar = typing.NewType(
    "JsonSimpleVar",
    bool | int | float | str | None
)
JsonComplexVar = typing.NewType(
    "JsonComplexVar",
    list[JsonSimpleVar] | dict[str, JsonSimpleVar]
)
JsonVar = typing.NewType(
    "JsonVar",
    JsonSimpleVar | JsonComplexVar
)