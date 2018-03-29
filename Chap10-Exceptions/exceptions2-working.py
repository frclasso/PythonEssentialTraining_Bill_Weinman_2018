#!/usr/bin/env python3


def main():
    try:
        x = 5/3  #ALTERNE O DIVISOR PARA ZERO(0)
    except ValueError:
        print('I caugth a ValueError!')
    except ZeroDivisionError:
        print("Don't divide by zero.")
    else:
        print('Good job!')
        print(x)


if __name__ == '__main__':main()
