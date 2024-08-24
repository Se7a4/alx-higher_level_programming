#!/usr/bin/python3
"""defins a class Rectangle."""


class Rectangle():
    """class that defines the properties of a rectangle.

    Attribute:
        width: the width of the rectangle.
        height: the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """creates an instance of a Rectangle class
        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Holds the width of a rectangle
        Returns: the width if the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width value
        Args:
            value: the value of the width given.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Holds the height of a rectangle
        Returns: the height if the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height value
        Args:
            value: the value of the height given.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that calculate the rectangle area.
        Returns:
            the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculate the rectangle perimeter
        Returns:
            the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height)*2
