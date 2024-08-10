#!/usr/bin/python3
""" Define a class named square """

class Square:
    """ a class Square that defines a square by: (based on 1-square.py)

    Attributs :
        size: size of square that must be an int and > 0
    """
    def __init__(self, size=0):
        """ creats an instance of a class Square.
        Args:
            size: size of the square
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError ("size must be an integer")
        elif self.__size < 0 :
            raise ValueError ("size must be >= 0")
        else:
            self.__size =size
