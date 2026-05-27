#!/usr/bin/env python3
"""This module defines a CustomObject class 
that can be serialized and deserialized using the pickle module."""
import pickle


class CustomObject:
    """Class representing a custom object"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PicklingError, EOFError, Exception) as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            
            if isinstance(obj, cls):
                return obj
            else:
                return None
        
        except (IOError, pickle.UnpicklingError, EOFError, Exception) as e:
            return None
