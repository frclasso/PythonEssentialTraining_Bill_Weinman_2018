#!/usr/bin/env python3

x = [1,2,3,4,5]     #Se fosse Tupla () daria erro
                    #TypeError: 'tuple' object does not support item assignment
x[2] = 42
for i in x:
    print('i is {}'.format(i))