class Shapes:
    def __init__(self, name, side, type, size):
        self.name = name
        self.side =side
        self.type = type
        self.size = size

    def move(self):
        print("I am a :" + self.name + "\n" +
              "I have :" + self.side + "sides" + "\n" 
              "I am a :" + self.type + "\n" +
              "I have :" + self.size + "\n")


objShapes = Shapes('shape', '0', 'circle', 'radius')
objShapes.move()


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14 * self.radius * self.radius
        return result


obj_coin = Circle(7)
print("The area of a coin is : ", obj_coin.area())

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        result = 1/2 * self.base * self.height
        return result

obj_pyramid = Triangle(3, 5)
print("The area of a pyramid is :", obj_pyramid.area())

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area (self):
        result = self.length * self.width
        return result
obj_laptop = Rectangle (5, 3)
print("The area of a laptop is :", obj_laptop.area())

class Square(Shapes):
    def __init__(self, side1, side2):
        self.side1 = side1
        self. side2 = side2
    def area(self):
        result = self.side1 * self.side2
        return result
obj_packet = Square(5, 5)
print("The area of a packet :", obj_packet.area())

