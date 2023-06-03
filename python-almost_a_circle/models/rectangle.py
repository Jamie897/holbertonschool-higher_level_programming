#!/usr/bin/python3
"""
class Rectangle(Base):

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
ls__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic
    of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are
    able to validate what a developer is trying to assign to a variable.
    So after, in your class you can “trust” these attributes.
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property width to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property height to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Property x to retrieve it"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Property y to retrieve it"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """This is the function that does area"""
        return self.__width * self.__height

    def display(self):
        """This function displays the rectangle"""
        print("\n" * self.__y, end='')
        for row in range(self.__height):
            print(" " * self.__x, end='')
            for col in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """This function overwrites __str__ of base"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """This function updates something"""
        if args:
            attr_names = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Function to return dict def of Rect"""
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}