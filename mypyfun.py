#!/usr/bin/env python3

from typing import Union, Sequence


def g(x: Union[float | Sequence]) -> Union[float | Sequence]:
    return x * 2


def f(y: Any) -> Any:
    return g(y)


print(f(10))
print(f('a'))
