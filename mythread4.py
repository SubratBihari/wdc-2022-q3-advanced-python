#!/usr/bin/env python3

# future -- a proxy for an answer that will (eventually) come

import threading
import time
import random

from concurrent.futures import ThreadPoolExecutor, submit


def hello(n):
    print(f'{n} Hello!')
    print(f'{n} Goodbye!')


with ThreadPoolExecutor() as executor:
    all_results = []
    for i in range(10):
        result = executor.submit(hello, args=(i,))
        all_results.append(result)

    print(all_results)
