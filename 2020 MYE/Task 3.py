class Grocery:
    def __init__(self, name, cost, stock):
        self.__name = name
        self.__price = None
        self.__cost = cost
        self.__stock = stock

    def add_stock(self, change_in_stock):
        self.__stock += change_in_stock

    def subtract_stock(self, change_in_stock):
        self.__stock -= change_in_stock

    def calculate_final_price(self):
        self.__price = self.__cost * 1.07
        print(self.__price)

    def price(self):
        print(self.__price)

class ElectricalAppliance(Grocery):
    def __init__(self, name, cost, stock, power):
        super().__init__(name, cost, stock)
        self.__power = power

    def calculate_final_price(self):
        self.__price = (self.__cost * 0.8 if self.__power <= 10 else 1) * 1.07
        print(self.__price)

class Alcohol(Grocery):
    def __init__(self, name, cost, stock, type):
        super().__init__(name, cost, stock)
        self.__type = type

    def calculate_final_price(self):
        self.__price = (self.__cost * 1.2 if self.__type == 'beer' else 1.5) * 1.07
        print(self.__price)
        print(self._Grocery__price)



beer = Alcohol('corona', 10, 1, 'beer')
#beer.price()
beer.calculate_final_price()
#beer.price()

for each in beer.__dict__:
    print(each)



