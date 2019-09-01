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

###################################################

class Figure:
    def __init__(self, color = None, figure = None):
        self.color = color
        self.figure = figure

    def info(self):
        return 'The chosen figure is ' + self.figure

    def get_color(self):
        return self.figure + ' color is ' + self.color

class Rectangle(Figure):
    def __init__(self, height, width):
        super().__init__('red', 'rectangle')
        self.height = height
        self.width = width

    def square(self):
        print( 'Square of the rectangle is ' , self.width*self.height )

class Square(Figure):
    def __init__(self, side):
        super().__init__('blue', 'square')
        self.side = side

    def square(self):
        print( 'Square of the square is' , self.side**2 )

r = Rectangle(7,5)
s = Square(4)
print(r.info())
print(r.get_color())
print(r.square())
print(s.info())
print(s.get_color())
print(s.square())
