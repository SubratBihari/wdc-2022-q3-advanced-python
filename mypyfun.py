#!/usr/bin/env python3

def g(x):
    return x * 2


def f(y):
    return g(y)


print(f(10))
print(f('a'))
