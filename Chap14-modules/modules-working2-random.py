#!/usr/bin/env python3

import random


def main():
    # x = random.randint(1, 1000)
    # print(x)

    y = list(range(25))
    print(y)
    random.shuffle(y)
    print(y)


if __name__=="__main__":main()


"""Mais sobre modulos acessem: https://docs.python.org/3/library/
"""