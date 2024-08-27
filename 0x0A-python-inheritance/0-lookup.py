#!/usr/bin/python3
"""Function to return the methods and attributes of an opject."""


def lookup(obj):
    """
    Return:
        a list of the attributes and methods of an object.
    """
    return (dir(obj))
