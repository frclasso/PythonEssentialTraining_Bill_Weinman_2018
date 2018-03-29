#!/usr/bin/env python3

x = (1,2,3,4,5)
y = (6,7,8,9,10)
z = zip(x, y)
for a, b in z:print(f'{a} - {b}')