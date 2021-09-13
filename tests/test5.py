class Car():
    def __init__(self,company,model,year_made):
        self.company = company
        self.model = model
        self.year = year_made

car1 = Car('Tesla','Model S Plaid',2021)
print(car1.model)
print(car1.year)

setattr(car1,'year',2022)
print(car1.year)

