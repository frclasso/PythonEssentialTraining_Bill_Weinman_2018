#!/usr/bin/env python3


def main():
    x = 5
    print(id(x))
    kitten(x)
    print('in main x is {}'.format(x))


def kitten(a):
    print(id(a)) #resultado eh o mesmo id de 'x'
    a = 3
    print(id(a)) #apos alteracao gera um novo id
    print('Meow.')
    print(a)

if __name__=="__main__": main()
