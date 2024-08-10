#!/usr/bin/python3
"""Defines a class named Square"""

class Square:
    """
    class that defines properties of square by: (based on 2-square.py)
    
    Attributes:
        size : size of a square.
    """
    def __init__(self, size=0):
        """creats a new instance of square 
        
        Args :
            size : size of the square.
        """
        self.__size = size 

        if not isinstance(size, int):
            raise TypeError ("size must be an integer")
        elif size < 0 :
            raise ValueError ("size must be >= 0")
        else :
            self.__size = size

    def area(self):
        """public instance method that calculates the area of square.
        
        Returns: The current square area.
        """
        return (self.__size*self.__size)
