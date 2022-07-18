#!/usr/bin/env python3

from typing import Any


def g(x: Any):
    return x * 2


def f(y: Any):
    return g(y)


print(f(10))
print(f('a'))
