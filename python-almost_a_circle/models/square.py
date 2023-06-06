#!/usr/bin/python3
"""Square Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size=1, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        parts = [type(self).__name__, self.id, self.x,
                 self.y, self.size]
        res = "[{0}] ({1}) {2}/{3} - {4}".format(*parts)
        return res

    def update(self, *args, **kwargs):
        """Quick Update"""
        if (args is None or args == ()) and kwargs is not None:
            args = [kwargs.get("id"), kwargs.get("size"), kwargs.get("x"),
                    kwargs.get("y")]
        try:
            self.id = args[0] or self.id
            self.size = args[1] or self.size
            self.x = args[2] or self.x
            self.y = args[3] or self.y
        except IndexError:
            return

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Turn this rect into a dict"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
