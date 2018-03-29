#!/usr/bin/env python3


def main():
    x =dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr' )
    kitten(**x) # PASSSANDO O DICIONARIO 'x' COMO ARGUMENTO


def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow!!!')


if __name__=="__main__":main()