#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor, as_completed
import glob


def file_length(filename):
    total = 0

    with open(filename) as f:
        for one_line in f:
            total += len(one_line)

    return total


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        results = executor.map(file_length, glob.glob('*.txt'))

    print(f'Total is {sum(results)}')
