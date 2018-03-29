#!/usr/bin/env python3


def main():
    f = open('Nicolas-Sarcozy.txt', 'r')
    for line in f:
        print(line.rstrip())


if __name__=="__main__":main()