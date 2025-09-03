class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def getArea(self):
        print("The area of rectangle is", self.length * self.width)
print("1st rectangle")
r1 = Rectangle(13,9)
r1.getArea()

print("2nd rectangle")
r2 = Rectangle(25,18)
r2.getArea()