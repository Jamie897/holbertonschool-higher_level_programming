#!/usr/bin/python3
"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with #s."""
        for n in range(self.__y):
            print("")
        for row in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """Updates the attributes with the given values."""
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary version of self. """
        return dict(id=self.id, width=self.width, height=self.height,
                    x=self.x, y=self.y)
