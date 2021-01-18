class Shape:
    height = 52
    width = 48

    def area(self):
        return self.height * self.width 
        

test = Shape()
print(test.area())