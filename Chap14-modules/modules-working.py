#!/usr/bin/env python3

import sys, os


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    w = sys.platform
    print(w)

    z = os.name
    print(z)

    # y = os.getenv('PATH')  # imprime variaveis de ambiente
    # print(y)

    i = os.getcwd()  # imprime diretorio local
    print(i)


if __name__=="__main__":main()


"""Mais sobre modulos acessem: https://docs.python.org/3/library/
"""