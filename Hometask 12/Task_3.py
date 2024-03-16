# 3. Создать класс «Живое».
# Определить наследуемые классы – «лиса», «кролик» и «растение».
# Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет.
# Представитель каждого класса может умереть, если достигнет определенного возраста или для него не будет еды.
# Напишите виртуальные методы поедания и определения состояния живого существа
# (живой или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
class Living:
    def __init__(self, age_limit: int) -> None:
        self.age: int = 0
        self.age_limit: int = age_limit
        self.alive: bool = True

    def eat(self, food_type: str) -> None:
        """
        get food for animal
        :param food_type: str
        :return: None
        """
        pass

    def is_alive(self, food: str) -> None:
        """
        get animal is alive
        :param food: str
        :return: None
        """
        if self.age >= self.age_limit or not food:
            self.alive = False


class Fox(Living):
    def __init__(self) -> None:
        super().__init__(age_limit=5)

    def eat(self, food_type: str) -> None:
        """
        get food for Fox
        :param food_type: str
        :return: None
        """
        if food_type == "Rabbit":
            print("Fox eat Rabbit")
        else:
            print("Fox doesn't eat Rabbit")


class Rabbit(Living):
    def __init__(self) -> None:
        super().__init__(age_limit=3)

    def eat(self, food_type: str) -> None:
        """
        get food for Rabbit
        :param food_type: str
        :return: None
        """
        if food_type == "Plant":
            print("Rabbit eat Plant")
        else:
            print("Rabbit doesn't eat Plant")


class Plant(Living):
    def __init__(self) -> None:
        super().__init__(age_limit=10)

    def eat(self, food_type: str) -> None:
        """
        get food for Plant
        :param food_type: str
        :return: None
        """
        print("Plant absorbs sunlight")


fox = Fox()
rabbit = Rabbit()
plant = Plant()

fox.eat("Rabbit")
fox.is_alive("Rabbit")

rabbit.eat("Plant")
rabbit.is_alive("Plant")

plant.eat(None)
plant.is_alive(None)

print("Fox:", "alive" if fox.alive else "dead")
print("Rabbit:", "alive" if rabbit.alive else "dead")
print("Plant:", "alive" if plant.alive else "dead")
