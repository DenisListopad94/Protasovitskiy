# 2. Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд», «Автомобиль».
# Определить время и стоимость перевозки для указанных городов и расстояний
class Carrier:
    def __init__(self, speed: float, cost: float, distance: float) -> None:
        self.speed = speed
        self.cost = cost
        self.distance = distance

    def transport_time(self) -> float:
        """
        get time for some class
        :return: float
        """
        return self.distance / self.speed

    def transport_cost(self) -> float:
        """
        get cost for some class
        :return: float
        """
        return self.distance * self.cost


class Plane(Carrier):
    def __init__(self) -> None:
        super().__init__(speed=1000, cost=100, distance=500)


class Train(Carrier):
    def __init__(self) -> None:
        super().__init__(speed=500, cost=50, distance=500)


class Car(Carrier):
    def __init__(self) -> None:
        super().__init__(speed=100, cost=10, distance=500)


plane = Plane()
train = Train()
car = Car()

print(f'{plane.transport_time()} hours, {plane.transport_cost()} rubles')
print(f'{train.transport_time()} hours, {train.transport_cost()} rubles')
print(f'{car.transport_time()} hours, {car.transport_cost()} rubles')
