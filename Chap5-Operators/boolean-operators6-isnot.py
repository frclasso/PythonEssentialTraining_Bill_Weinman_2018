#!/usr/bin/env python3

#Exemplos utilizando operadores booleanos (and, or, not, in, not in, is , is not).

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky','rain')
y = 'bear'

if y is not x[1]:   # y(bear) is NOT x[1](bunny)
    print('Expression is true')
else:
    print('Expression is false')


