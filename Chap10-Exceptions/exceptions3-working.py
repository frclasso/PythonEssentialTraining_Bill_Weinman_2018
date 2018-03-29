#!/usr/bin/env python3


import sys


def main():
    try:
        x = 5/0  #ALTERNE O DIVISOR PARA ZERO(0)
    except ValueError:
        print('I caugth a ValueError!')
    except:
        print(f'UnkwonError:{sys.exc_info()[1]}')  # [1] pega nome do erro, delete [1]
                                                   # para ver completo
    else:
        print('Good job!')
        print(x)


if __name__ == '__main__':main()
