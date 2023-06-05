#!/usr/bin/python3
"""Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    @property
    def width(self):
        return self.__width or 0

    @width.setter
    def width(self, value):
        self.__width = Base.check_int(value, "width")

    @property
    def height(self):
        return self.__height or 0

    @height.setter
    def height(self, value):
        self.__height = Base.check_int(value, "height")

    @property
    def x(self):
        return self.__x or 0

    @x.setter
    def x(self, value):
        self.__x = Base.check_int(value, "x", 0)

    @property
    def y(self):
        return self.__y or 0

    @y.setter
    def y(self, value):
        self.__y = Base.check_int(value, "y", 0)

    def __init__(self, width=1, height=1, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculate Area of rect"""
        return self.width * self.height

    def display(self):
        """Draw a rectangle"""
        print("\n" * self.y, end="")
        for y_index in range(self.height):
                print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        parts = [type(self).__name__, self.id, self.x,
                 self.y, self.width, self.height]
        res = "[{0}] ({1}) {2}/{3} - {4}/{5}".format(*parts)
        return res

    def update(self, *args, **kwargs):
        """Quick Update"""
        if (args is None or args == ()) and kwargs is not None:
            args = [kwargs.get("id"), kwargs.get("width"),
                    kwargs.get("height"), kwargs.get("x"),
                    kwargs.get("y")]
        try:
            self.id = args[0] or self.id
            self.width = args[1] or self.width
            self.height = args[2] or self.height
            self.x = args[3] or self.x
            self.y = args[4] or self.y
        except IndexError:
            return

    def to_dictionary(self):
        """Turn this rect into a dict"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
