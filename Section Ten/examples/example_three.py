class Shape:
    def __init__(self):
        self.height = 10
        self.width = 6

    def area(self):
        return self.height * self.width 
        
class Triangle(Shape):
    def area(self):
        return (self.height * self.width) * .5
        

test = Triangle()
print(test.area())