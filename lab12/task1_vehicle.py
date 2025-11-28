from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Машина едет по дороге"

    def fuel_type(self):
        return "Бензин"


class Bicycle(Vehicle):
    def move(self):
        return "Велосипед движется с помощью педалей"

    def fuel_type(self):
        return "Не требует топлива"


car = Car()
bike = Bicycle()

print(car.move())
print(car.fuel_type())
print(bike.move())
print(bike.fuel_type())