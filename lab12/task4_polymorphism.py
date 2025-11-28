from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Машина едет"


class Bicycle(Vehicle):
    def move(self):
        return "Велосипед движется"


class Airplane(Vehicle):
    def move(self):
        return "Самолёт летит"


class Train(Vehicle):
    def move(self):
        return "Поезд движется по рельсам"


vehicles = [Car(), Bicycle(), Airplane(), Train()]

for v in vehicles:
    print(v.move())