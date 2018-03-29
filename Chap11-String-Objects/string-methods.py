#!/usr/bin/env python3

x = 42
y = 73

#print('The numbers are {} and {}'.format(x, y))

#print('The numbers are {xx} and {yy}'.format(xx =x, yy = y))

#print('The numbers are {0} and {1}'.format(x, y))

#print('The numbers are {1} and {0}'.format(x, y))

#print('The numbers are {0:<5} and {1:>5}'.format(x, y))  # 5 posicoes

#print('The numbers are {0:<5} and {1:>005}'.format(x, y))  # 5 posicoes, 00073

z = 42 * 747
w = z * 1000
#print('the number is {:,}'.format(z))
#print('the number is {:,}'.format(w))
#print('the number is {:,}'.format(w).replace(',', '.'))
#print('the number is {:.3f}'.format(w))

print('the number is {:x}'.format(x))  # HEXADECIMAL
print('the number is {:o}'.format(x))  # OCTAL
print('the number is {:b}'.format(x))  # BINARIO

print(f'the number is {x:.3f}')  # FORMATO PYTHON 3.6
