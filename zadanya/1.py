#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создать класс Liquid (жидкость), имеющий поля названия и плотности. Определить методы
переназначения и изменения плотности. Создать производный класс Аlcohol (спирт),
имеющий крепость. Определить методы переназначения и изменения крепости.
"""


class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def set_density(self, density):
        self.density = density

    def display(self):
        print(f"Жидкость: {self.name}, Плотность: {self.density} g/cm³")


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def set_strength(self, strength):
        self.strength = strength

    def display(self):
        super().display()
        print(f"Крепость алкоголя: {self.strength}%")


if __name__ == '__main__':
    water = Liquid("Вода", 1.0)
    water.display()

    vodka = Alcohol("Водка", 0.789, 40)
    vodka.display()

    # Изменение плотности и крепости
    water.set_density(0.998)
    vodka.set_strength(50)

    # Вывод измененных данных
    print("\nПосле модификации:")
    water.display()
    vodka.display()
