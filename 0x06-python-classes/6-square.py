#!/usr/bin/python3
"""Defins a class named Square"""


class Square:
    """
    Class that defines the properties of a square by: (based on 4-square.py).

    Attributes:
        size: size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creats an instance from Square class

        Args:
            __size(int): size of the square.
            __position(tuple): position of the square.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of the square.

        Return: returns the current square area.
        """
        return self.__size ** 2

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

    @property
    def position(self):
        """Return: returns the position of square.
        """
        return self.position

    @position.setter
    def position(self, value):
        """A setter for the position value
        Args:
            value(tuple): a tuple of 2 positive integers.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple(+int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
