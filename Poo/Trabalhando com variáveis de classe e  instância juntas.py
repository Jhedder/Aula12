class Shark:
    animal_type = "Fish"
    location = "Ocean"
    followers = 0
    
    def __init__(self, name_p, age_p):
        self.name = name_p
        self.age = age_p

    
    def set_followers(self,followers_p):
        self.followers = followers_p
        print(f"This user has {self.followers} followers.")
    def set_name(self,name_p):
        self.name = name_p
    def clean_all(self):
        self.animal_type = ""
        self.location = ""
        self.followers = 0
        self.name = ""
        self.age = 0

newname_shark = Shark("Doidão",5)
print(newname_shark.name)
newname_shark.set_name("Benny")
print(newname_shark.name)



new_shark = Shark("Doidão",5)

print(new_shark.followers)#0
new_shark.set_followers(5)
print(new_shark.followers)#5


new_shark.clean_all()
print(new_shark.name)


