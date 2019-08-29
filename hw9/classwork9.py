class Animal:
    def __init__(self, paws, anm, sound):
        self.anm = anm
        self.paws = paws
        self.sound = sound
class Rabbit(Animal):
    def __init__(self):
        super().__init__("rabbit", 4, "clucks")
    def snd(self):
        return 'Rabbit clucks'
class Mockingbird(Animal):
    def __init__(self):
        super().__init__("mockingbird", 2, "mimics")
    def snd(self):
        return 'Mockingbird mimics'

# Class Figure:
#     def __init__(self, color):

    