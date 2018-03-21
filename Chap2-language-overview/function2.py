#!/usr/bin/env python3


def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


def list_primes():
        for n in range(100):
            if isPrime(n):
                print(n, end=' ', flush=True)

        print()


list_primes()

#
# n =6
# if isPrime(n):
#     print('{} is Prime'.format(n))
# else:
#     print('{} is not prime'.format(n))