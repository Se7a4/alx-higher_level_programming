#!/usr/bin/python3
""" Define a class named square """

class Square:
    """ a class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        """ Define an instance from a class Square.

        Attributs :
        size: size of square that must be an int and > 0.
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError ("size must be an integer")
        elif self.__size < 0 :
            raise ValueError ("size must be >= 0")
