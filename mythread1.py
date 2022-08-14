#!/usr/bin/env python3

import threading


def hello():
    print('Hello!')


for i in range(10):
    # create a thread object, which will run hello
    t = threading.Thread(target=hello)

    # actually run the function in a new thread
    t.start()
