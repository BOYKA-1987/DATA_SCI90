class Car:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price

    def display(self):
        print(f"name of car is {self.name} and model is {self.model} and its price is {self.price}.")
        