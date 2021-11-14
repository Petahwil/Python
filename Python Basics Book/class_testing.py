#!/usr/bin/env python
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
# Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def __repr__(self):
        return f'Dog(name={self.name}, age={self.age})'

# class WidgitWithoutStr:
#     """
#     A class with no __str__ or __repr__ methods defined.
#     """
#     def __init__(self, name):
#         self.name = name

# class WidgitWithStrOnly(WidgitWithoutStr):
#     """
#     A class with __str__ defined.
#     """
#     def __str__(self):
#         return self.name

# class WidgitWithReprOnly(WidgitWithoutStr):
#     """
#     A class with __repr__ defined.
#     """
#     def __repr__(self):
#         return "{}({})".format(self.__class__.__name__, self.name)

# print(WidgitWithoutStr("Nobody")) # <__main__.WidgitWithoutStr object at 0x10b8c1790>
# print(WidgitWithStrOnly("Bob")) # Bob
# print(WidgitWithReprOnly("Mary")) # WidgitWithReprOnly(Mary)