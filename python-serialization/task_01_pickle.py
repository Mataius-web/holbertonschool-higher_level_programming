#!/usr/bin/env python3
"""Module to serialize and deserialize an object and its content
    with Pickle"""
import pickle


class CustomObject:
    """Class represents a custom object"""
    def __init__(self, name, age, is_student):
        self.custname = name
        self.custage = age
        self.custis_student = is_student

    def display(self):
        print(f"Name: {self.custname}")
        print(f"Age: {self.custage}")
        print(f"Is Student: {self.custis_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to a file using Pickle"""
        try:
            with open(f"{filename}", "wb") as f:
                pickle.dump(self, f)
                return None
        except (IOError, pickle.PicklingError, EOFError, Exception) as e:
            print(f"Cant write in {filename}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file using Pickle"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (IOError, pickle.UnpicklingError, EOFError, Exception) as e:
            print(f"Cant read {filename}")
            return None
