#!/usr/bin/env python3

#x = '47'
x = 47
#y = int(x)
#y = float(x)
#y = divmod(x, 3)  # DIVIDE INT ou FLOAT primeiro argumento pelo segundo

#y = x + 73j  # CRIA UM NUMERO COMPLEXO 47+73J
y = complex(x, 73)  # USA A FUNCAO BUILT IN COMPLEX PARA CRIAR O MESMO NUM COMPLEXO


print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'x is {y}')


"""Para mais informacoes e exemplos de Funcoes Built-in acessem:
   https://docs.python.org/3/library/functions.html
"""