#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = "Nicolas"
        self.age = 32
        self.is_student = True

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PicklingError, OSError) as e:
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
        
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None
