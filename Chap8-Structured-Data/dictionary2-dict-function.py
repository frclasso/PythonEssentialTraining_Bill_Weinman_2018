#!/usr/bin/env python3


def main():

    # UTILIZANDO A FUNCAO 'dict'PARA CRIAR UM DICIONARIO
    animals = dict(kitten ='meow', puppy='ruff', lion='grrr',
                         giraffe='I am giraffe!', dragon='rawr')

    print_dict(animals)


def print_dict(o):
    for x in o:print(f'{x}: {o[x]}')


if __name__ == "__main__":main()