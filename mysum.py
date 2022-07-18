#!/usr/bin/env python3

def mysum(numbers: list[float]) -> float:
    total: float = 0

    for one_number in numbers:
        total += one_number

    return total


print(mysum([10, 20, 30]))
print(mysum([10, 20.5, 30]))
print(mysum([10, 'a', 30]))
print(mysum([10, 20, [1, 2, 3]]))
print(mysum((100, 200, 300)))
