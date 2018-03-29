#!/usr/bin/env python3


def main():
    try:
        x = int('foo')
    except ValueError:
        print('I caugth a ValueError!')


if __name__ == '__main__':main()
