#!/usr/bin/python3
""" Define a class named square """


class Square:
    """
    A class that defines the attributes of square 

    Attributes:
    size: size of the square
    """
    
    def __init__(self , size):
        """ creat new instance of square.

        Args: 
            size: size of the square
        """
        self.__size = size