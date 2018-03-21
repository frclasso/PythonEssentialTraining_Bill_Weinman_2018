#!/usr/bin/env python3

x = 42
y = 73

if x < y:
    print('x < y: x is {}  and y is {}'.format(x, y))
elif x > y:
    print(('x > y: x is {} and y is {}'.format(x, y)))
elif x == y:
    print('x = y: x is {} and y is {}'.format(x, y))
else:
    print('Something else')