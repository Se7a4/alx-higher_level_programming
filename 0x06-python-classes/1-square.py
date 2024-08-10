#!/usr/bin/python3
""" define a class named square """


class Square():
    """ define a class attripute.

    Args: 
        size: size of the square
    """
    __size = None

    """ creat new instance of square."""
    def __init__(self , size):
        self.__size = size