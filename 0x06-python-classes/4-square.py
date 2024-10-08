#!/usr/bin/python3
"""Define a calss named square."""


class Square:
    """Class that defines properties of square by: (based on 3-square.py)

    Attributes:
        size: size of square.
    """

    def __init__(self, size=0):
        """Creats an instance from Square class

        Args:
            size: size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Return: returns the size value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter for the size.

        Args:
            value: holds the value of the size.

        Raises:
            TypeError: size must be an integer
            ValueError: "size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.

        Return: returns the current square area.
        """
        return self.__size ** 2
     