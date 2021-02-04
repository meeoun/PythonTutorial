from Person import Person
from random import choice
from example.Animal import Animal

things = ['phone', 'stapler', 'cat']
person = Person()
animal = Animal()
print(person.first_name)
print(choice(things))
print(animal.width)