#!/usr/bin/env python3

from typing import Union, Sequence, Any


def g(x: Union[float | Sequence[str]]) -> Union[float | Sequence[str]]:
    return x * 2


def f(y: Any) -> Any:
    return g(y)


print(f(10))
print(f('a'))
