#!/usr/bin/env python3

x = 0x0a
y = 0x02

z = x & y 


print('(hex) x is {:02x} , y is {:02x}, and z is {:02x}'.format(x,y,z) )
print('(bin) x is {:08b}, y is {:08b}, and z is {:08b}'.format(x, y, z))

#Novidade Python 3.6.4  f' substitui .format
#print(f'(hex) x is {x:02x} , y is {y:02x}, and z is {z:02x}' )
#print(f'(bin) x is {x:08b}, y is {y:08b}, and z is {z:08b}')

