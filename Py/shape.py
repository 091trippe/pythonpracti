from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def area(self):
        return self._length * self._width

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def area(self):
        return math.pi * self._radius ** 2

def main():
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Rectangle(7, 2),
        Circle(1.5),
    ]

    for shape in shapes:
        print(f"Площа фігури {type(shape).__name__}: {shape.area():.2f}")

if __name__ == "__main__":
    main()
