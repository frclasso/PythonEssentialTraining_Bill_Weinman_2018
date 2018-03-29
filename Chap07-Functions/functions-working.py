#!/usr/bin/env python3


def main():
    x = kitten()
    print(type(x), x)


def kitten():
    print('Meow!!!!!!')
    return dict(x = 42, y=43, z=44)


if __name__=="__main__":main()



