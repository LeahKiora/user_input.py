class Person:
 def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

#Creating an instance of the person class
person = Person("Leah Kiora", 26, "Female")

#Displaying the introduce
person.introduce()