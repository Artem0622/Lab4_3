#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создать абстрактный базовый класс Body (тело) с абстрактными функциями вычисления
площади поверхности и объема. Создать производные классы: Parallelepiped
(параллелепипед) и Ball (шар) со своими функциями площади поверхности и объема.
"""


from abc import ABC, abstractmethod
from math import pi


class Body(ABC):
    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

    def __str__(self):
        return f"Площадь поверхности: {self.surface_area()}\nОбьём: {self.volume()}"


class Parallelepiped(Body):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return f"Параллелипипед:\n{super().__str__()}"


class Ball(Body):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * pi * self.radius**2

    def volume(self):
        return (4 / 3) * pi * self.radius**3

    def __str__(self):
        return f"Ball:\n{super().__str__()}"


if __name__ == "__main__":
    parallelepiped = Parallelepiped(3, 4, 5)
    print(parallelepiped)

    print("\n------------------\n")

    ball = Ball(2)
    print(ball)
