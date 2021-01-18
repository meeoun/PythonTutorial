class Shape:
    def __init__(self):
        self.height = 52
        self.width = 48

    def area(self):
        return self.height * self.width 
        

test = Shape()
print(test.area())