# A car class
class Car:

    # Constructor
    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    # For call to str(). Prints readable form
    def __str__(self):
        pass


# A store class
class Store:

    # Constructor
    def __init__(self):
        self.price_list = []
        self.cash = 0

    # For call to str(). Prints readable form
    def __str__(self):
        pass

    def add_car(self, manufacturer, model, price):
        self.price_list.append(Car(manufacturer, model, price))

    def sell_car(self, manufacturer, model):
        pass


# store01 = Store
#
# store01.add_car()
# store01.add_car()
# store01.add_car()
#
# print(store01)
#
# store01.sell_car()
