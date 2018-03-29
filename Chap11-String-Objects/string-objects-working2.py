#!/usr/bin env python3

s = 'Hello World!'
s2 = s.upper()
s3 = 'Another string'
s4 = 'this string' ' or' ' that string'

print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.casefold()) # similar a lower, no entanto mais poderoso

print()
print(id(s))
print(id(s2))  # podemos verificar que foi criado um novo objeto

print()
print(s + ' ' + s3) # concatenando strings
print()
print(s4)