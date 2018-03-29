#!/usr/bin/env python3


def f1(f):
    def f2():
        print('This is before function call')
        f()
        print('This is after function call')
    return f2

@f1 #DECORATOR
def f3():
    print("This is f3")

f3()