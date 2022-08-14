#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, as_completed
import glob


def file_length(filename):
    total = 0

    with open(filename) as f:
        for one_line in f:
            total += len(one_line)

    return total


file_length_total = 0

with ThreadPoolExecutor() as executor:
    all_results = []
    for one_filename in glob.glob('*.txt'):
        result = executor.submit(file_length, one_filename)
        all_results.append(result)

    for one_result in as_completed(all_results):
        file_length_total += one_result.result()

print(f'Total is {file_length_total}')
