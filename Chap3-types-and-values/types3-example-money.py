#!/usr/bin/env python3

x = .1 + .1 + .1 - .3  #x is 5.551115123125783e-17  onde e-17 qunatidade poicoes apos o ponto
print('x is {}'.format(x))
print(type(x))

print('-'* 15)

from decimal import  *

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
