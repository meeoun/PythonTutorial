class Arm:
    def __init__(self):
        self.length = 40


class Leg:
    def __init__(self):
        self.length = 80


class Robot:
    def __init__(self):
        self.leftArm = Arm()
        self.rightArm = Arm()
        self.leftleg = Leg()
        self.rightLeg = Leg()
        
    # Magic method that compares the object to another
    # object of the same type.
    def __eq__(self, other):
        return self.leftArm.length == other.leftArm.length 


test = Robot()
test2 = Robot()
print(test.leftArm.length)
print(test == test2)