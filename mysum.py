#!/usr/bin/env python3

def mysum(numbers: list[int]) -> int:
    total = 0

    for one_number in numbers:
        total += one_number

    return total


print(mysum([10, 20, 30]))
print(mysum([10, 'a', 30]))
print(mysum([10, 20, [1, 2, 3]]))
print(mysum((100, 200, 300)))
