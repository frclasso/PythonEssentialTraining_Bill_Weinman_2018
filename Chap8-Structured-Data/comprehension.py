#!/usr/bin/env python3


def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]  # Criando uma lista dos elementos de seq multiplicados por 2
    # seq2 = [x for x in seq if x % 3 != 0] # Imprime os elementos de seq nao divisiveis por 3
    # seq2= [(x, x**2) for x in seq] # Cria tuplas com o numero original  e seu quadrado

    '''seq2 = {x: x**2 for x in seq} # criando um dicionario  a partir de seq
    print(seq2)'''

    # seq2 = {x for x in 'superduper' if not x in 'pd'} # Imprime os caracteres incomuns as strings

    print_list(seq)
    print_list(seq2)


def print_list(o):
    for x in o: print(x, end=' ')
    print()


if __name__ == "__main__":main()