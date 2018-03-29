#!/usr/bin/env python3

s = 'This is a long string with a bunch of words in it.'
l = s.split()
print(l)

s2 = '--'.join(l)
print(s2)

s3 = s.split('i')
print(s3)
