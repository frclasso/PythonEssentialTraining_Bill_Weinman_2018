#!/usr/bin/env python3

#Exemplos utilizando operadores booleanos (and, or, not, in, not in, is , is not).

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky','rain')
y = 'bear'

if y is x[0]:   # y(bear) is x[0](bear)
    print('Expression is true')
else:
    print('Expression is false')


print(id(x[0]))  #MESMO ID, MESMO OBJETO
print(id(y))
