#!/usr/bin/env python3

import datetime


def main():
    now= datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day,now.hour, now.minute, now.second)
    print(f'Calendar {now.year}/{now.month}/{now.day}  and Clock {now.hour}:{now.minute}:{now.second}')


if __name__=="__main__":main()


"""Mais sobre modulos acessem: https://docs.python.org/3/library/
"""