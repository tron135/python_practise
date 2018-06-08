class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f'Name is {self.name} and Age is {self.age}')

class teacher(person):
    def print(self,name,age):
        person.__inti__(self,name,age)
