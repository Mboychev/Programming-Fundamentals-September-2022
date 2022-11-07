# Create a class Vehicle. The __init__ method should receive a type, a model, and a price.
# You should also set an owner to None. The class should have the following methods:
# •	buy(money: int, owner: str)
# o	If the person has enough money and the vehicle has no owner,
# returns: "Successfully bought a {type}. Change: {change}" and sets the owner to the given one
# o	If the money is not enough, return: "Sorry, not enough money"
# o	If the car already has an owner, return: "Car already sold"
# •	sell()
# o	If the car has an owner, set it to None again.
# o	Otherwise, return: "Vehicle has no owner"
# •	__repr__()
# o	If the vehicle has an owner, returns: "{model} {type} is owned by: {owner}".
# o	Otherwise, return: "{model} {type} is on sale: {price}"

class Vehicle:

    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):

        if self.owner != None:
            return "Car already sold"

        elif self.price > money:
            return "Sorry, not enough money"

        else:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if self.owner != None:
            self.owner = None

        elif self.owner == None:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
