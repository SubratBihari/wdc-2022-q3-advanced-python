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
    results = executor.map(file_length, glob.glob('
    
    all_futures = []
    for one_filename in glob.glob('*.txt'):
        future = executor.submit(file_length, one_filename)
        all_futures.append(future)

    for one_future in as_completed(all_futures):
        file_length_total += one_future.result()    # result is a future method

print(f'Total is {file_length_total}')
