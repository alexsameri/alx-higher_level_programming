#!/usr/bin/python3
class MyList(list):
    """Represents a MyList"""
    def print_sorted(self):
        """Prints the list but sorted"""
        print(sorted(self))
