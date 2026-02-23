class dog:
    species = "canis familiaris"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def display_details(self):
        print(f"Dog Breed: {self.breed}")
        print(f"Dog Name: {self.name}")
        print(f"Species: {dog.species}")
        print("-------------------------------")

dog1 = dog("Labrador", "Buddy")
dog2 = dog("German Shepherd", "Max")

dog1.display_details()
dog2.display_details()