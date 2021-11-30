class Person:
    def __init__(self, name, age, country, gender):
        self.name = name
        self.age = age
        self.country = country
        self.gender = gender
    def get_person_details(self):
        print(f"{self.name} is {self.age} years old and from {self.country}")

class Hobby(Person):
    def __init__(self, name, age, country, gender, interest):
        super().__init__(name, age, country, gender)
        self.interest = interest

    def get_hobby_details(self):
        #print(f"Hobby is {self.interest}")
   #     Person.get_person_details()
        print(f"{self.name} is {self.age} old and from {self.country} and interest is :{self.interest}")

class AllDetails(Person):
        def display(self):
            Person.get_person_details(self)
            self.age += 1
            print(f"Age is increased by 1 : {self.age}")
    #def display(self):

     #   print(f"{self.name} is {self.age} old and from {self.country}")



'''
p1 = Person("Janu", 30, "USA", "Female")
p2 = Person("Sam", 33, "USA", "Male")
p1.get_person_details()
p2.get_person_details()
h1 = Hobby("cooking")
#print(h1.interest)
'''
#h2 = Hobby("History")
h1 = Hobby ("janu", 30, "USA", "Female","cooking")
h1.get_hobby_details()
print(h1.age)
#p1.get_hobby_details()
#p2.get_hobby_details()

c = AllDetails("asg", 55, "insga", "male")
c.display()
print(c.age)
c.display()