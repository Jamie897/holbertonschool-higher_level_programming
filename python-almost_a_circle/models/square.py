#!/usr/bin/python3
"""
class Square that inherits from Rectangle:

Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None):
Call the super class with id, x, y, width and height -
    this super call will use the logic of the __init__ of the
    Rectangle class. The width and height must be assigned to
    the value of size
You must not create new attributes for this class, use all
    attributes of Rectangle - As reminder: a Square is a Rectangle
    with the same width and height
All width, height, x and y validation must inherit from Rectangle -
    same behavior in case of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> -
    <size> - in our case, width or height
As you know, a Square is a special Rectangle, so it makes sense this
    class Square inherits from Rectangle. Now you have a Square class
    who has the same attributes and same methods.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size/width"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for width and height, aka size"""
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """This function updates something"""
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Function to return dict def of Rect"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}