import this


class parent:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        a=self.name
        b=self.age

    def update(self,nameU,ageU):
        self.name=nameU
        self.age=ageU
    
    def getDetails(self):
        print(f'Name: {self.name}\nAge: {self.age}')


p1=parent('Anirban',19)
# print(id(p1)) # --> It'll give the memory address of p1
p1.getDetails()

p1.update('Rahul',20)
p1.getDetails()