# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    def bark(self):
        print("Woof!")
        

# instantiation call that creates a Dog object:
# Dog("Rex")

# the same instantiation call that creates a Dog object,
# but now we've assigned it to the value of the my_dog variable
# my_dog = Dog("Rex", "SuperDog")
# print(my_dog)
# print(my_dog.name)

# add "breed" property on the fly
# my_dog.breed = "SuperDog"
# will print "SuperDog"
# print(my_dog.breed)

# my_dog.bark()
