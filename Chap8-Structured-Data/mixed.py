#!/usr/bin/env python3

# using set


def main():

    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry Dave. I'm afraid I can't do it.")
    print_set(a)
    print_set(b)
    # print_set(sorted(a))
    # print_set(sorted(b))
    #print_set(a - b) # MEMBROS DE A QUE NAO ESTAO EM B
    #print_set(a | b)  # MEMBROS DE UM OU AMBOS OS SET'S
    #print_set(a ^ b) # OU EXCLUSIVO, UM OU OUTRO, NAO AMBOS

    # print_set(a & b)  # MEMBROS DE AMBOS

def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')

if __name__ == "__main__":main()