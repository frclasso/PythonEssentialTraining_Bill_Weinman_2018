#!/usr/bin/env python3

import time


def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print("Elapsed time: {} ms".format((t2 -t1)*1000))
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print('Big Sum: {}'.format(sum(num_list)))


def main():
    big_sum()


if __name__=="__main__":main()