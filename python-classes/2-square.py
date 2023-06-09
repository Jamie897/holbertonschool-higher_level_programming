#!/usr/bin/python3
"""
Write a class Square that defines a square

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0)
"""


class Square():
    """
    Defines a square with a private instance attribute
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
