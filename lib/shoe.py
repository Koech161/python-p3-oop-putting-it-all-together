#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")

    def __str__(self):
        return f'Brand: {self.brand}, Size: {self.size}, Condition: {self.condition}'
