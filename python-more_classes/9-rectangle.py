#!/usr/bin/python3
"""
    Rectangle module
    """


class Rectangle:
    """
        Rectangle Class
        Attribute:
            width (int): Private
            height (int) : Private
            number_of_instances (int): Public
            print_symbol (str): Public
        """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Init Rectangle Class
        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
            number_of_instance (int): The number of instances
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            width getter
            Return: The width of the Rectangle (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width setter
        Args:
            Value (int) : a value to set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            height getter
        Return: the height of the rectangle (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
        Args:
            value (int) : value to be set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            a function that calculate area of a rect
        Returns:
            area of a rect
        """
        return self.__height * self.__width

    def perimetre(self):
        """
          a function that calculate perimeter of a rect
        Returns:
            perimetre of a rect
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
            print the rectangle
        Returns:
            printed rectangle with "#"
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return ((print_symbol * self.__width + '\n') * self.__height)[:-1]

    def __repr__(self):
        """
            string representation of the rectangle
        Return:
            (str) representation of the rectangle
        """
        return 'Rectangle ({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
            Print message when instances are deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            compare 2 rectangle
        Args:
            rect_1(Rectangle): First rectangle
            rect_2(Rectangle): Second Rectangle
        Raises:
            TypeError: If rect_1/rect_2 is not instance ofrectangle
        Return:
            Biggest rectangle (rectangle)
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

    @classmethod
    def square(cls, size):
        """
        Makea square from a rectangle
        Args:
            size(int): the size of thge square
        Returns:
            (Rectangle): instaance of rectangle
        """
        return cls(size, size)
