#!/usr/bin/env python3



#Fibonacci series

a, b = 0, 1
while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a + b

print()  #line ending