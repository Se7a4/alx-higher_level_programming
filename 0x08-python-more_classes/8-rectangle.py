#!/usr/bin/python3
"""defins a class Rectangle."""


class Rectangle():
    """class that defines the properties of a rectangle.

    Attribute:
        width: the width of the rectangle.
        height: the height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """creates an instance of a Rectangle class
        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def print_rectangle(self):
        """printing '#' alike the real shape of the rectangle.
        Returns:
            returns the '#' as the area of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for row in range(self.__height):
            rectangle_str += str(self.print_symbol)*self.__width
            if row < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __str__(self):
        """viewing a readable output for the user
        Returns:
            the print_recatngle method output.
        """
        return self.print_rectangle().rstrip()

    def __repr__(self):
        """the output is only readable for developer.
        Returns:
            the canonical string representation of the object.
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """deleting the instance of a rectangle."""
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare between two rectangles's area to returns the bigger
        Args:
            rect_1: the first rectangle passed.
            rect_2: the second rectangle passed.
        Returns:
            the bigger area and if they are equal returns rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        return rect_2
