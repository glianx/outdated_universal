class Car():
    def __init__(self,company,model,year,hp):
        self.company = company
        self.model = model
        self.year = year
        self.hp = hp
        self.hpx2 = 2 * self.hp

    def describe(self):
        print(self.company,self.model,self.year)

car1 = Car('Tesla','Model X',2021,600)
car2 = Car('Porsche','Taycan',2020,750)

print(car2.hpx2)
setattr(car2,'hp',800)
print(car2.hp)
car2.hpx2
print(car2.hpx2)