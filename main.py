class Cats:
    def __init__(self, type, name, gender, colour, age):
        self.type = type
        self.name = name
        self.gender = gender
        self.colour = colour
        self.age = age
    def move(self):
        print("I am a:" + self.type + "\n" +
              "My name is:" + self.name + "\n" +
              "My gender is:" + self.gender + "\n" +
              "My colour is:" + self.colour + "\n"
              "My age is:" + self.age)
objCats=Cats("Lion", "White Lion", "Female", "Orange", "5 Years Old")
objCats.type= "Wild Cat" #this is to target
objCats.move()
class Lion(Cats): #this is to show inheritance
    pass
class Tiger(Lion):
    pass

