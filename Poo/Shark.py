""""
class Shark:
    animal_type = "Fish"
    location = "Ocean"
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)"""""

class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Doidão",5)
print(new_shark.name)
print(new_shark.age)