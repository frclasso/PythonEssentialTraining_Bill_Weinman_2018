#!/usr/bin/env python3


def main():
    x = ('meow', 'gurr', 'purr', 'hello', 'world')
    kitten(*x)


def kitten(*args):
    if len(args): #caso tenha pelo menos um argumento
        for s in args:
            print(s)
    else:
        print('Meow!!!') #caso Kitten nao receba nenhum parametro


if __name__ == "__main__": main()