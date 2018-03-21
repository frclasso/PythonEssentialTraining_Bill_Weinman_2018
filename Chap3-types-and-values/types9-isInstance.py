#!/usr/bin/env python3

x = [1, 'two', 3.0, [4,'four'], 5]
y = (1, 'two', 3.0, [4,'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(id(x))

print('-' * 15)

print('y is {}'.format(y))
print(type(y))
print(id(x))

print('-' * 15)

if isinstance(y, tuple):
    print('Tuple')
elif isinstance(y, list):
    print('List')
else:
    print('Nope')