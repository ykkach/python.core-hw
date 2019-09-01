class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def info(self):
        return f"{name}s age is {age}"