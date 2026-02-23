class car:
    wheels = 4 

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Wheels: {car.wheels}")
        print("-------------------------------")

car1 = car("Toyota", "Corolla")
car2 = car("Honda", "Civic")

car1.display_details()
car2.display_details()