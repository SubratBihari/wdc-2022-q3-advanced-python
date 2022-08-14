#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, as_completed
import glob


def file_length(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    return total


with ThreadPoolExecutor() as executor:
    all_results = []
    for one_filename in glob.glob('*.txt'):
        result = executor.submit(file_length, i)
        all_results.append(result)

    for one_result in as_completed(all_results):
        print(one_result.result())
