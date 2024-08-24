#!/usr/bin/python3
"""Defines an integer addtion function"""


def (a, b=98):
    """An addtion function

    Return: returns the addtion value(integers)
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
    return int(a+b)


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/0-add_integer.txt')
