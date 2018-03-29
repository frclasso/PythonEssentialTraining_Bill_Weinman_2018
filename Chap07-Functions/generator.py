#!/usr/bin/env python3


def main():
    for i in inclusive_range(25):
        print(i, end=" ")
    print()


def inclusive_range(*args):
    numargs = len(args)
    start= 0
    step =1

    #intialize parameters
    if numargs < 1:
        raise TypeError('Expected at least 1 argument,got {}'.format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('Expected at most 3 arguments, got {}'.format(numargs))

    #generator
    i = start
    while i <= stop:
        yield i
        i += step


if __name__=="__main__": main()