# 3. Создать класс «Живое».
# Определить наследуемые классы – «лиса», «кролик» и «растение».
# Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет.
# Представитель каждого класса может умереть, если достигнет определенного возраста или для него не будет еды.
# Напишите виртуальные методы поедания и определения состояния живого существа
# (живой или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
class Living:
    def __init__(self, age_limit):
        self.age = 0
        self.age_limit = age_limit
        self.alive = True

    def eat(self, food_type):
        pass

    def is_alive(self, food):
        if self.age >= self.age_limit or not food:
            self.alive = False


class Fox(Living):
    def __init__(self):
        super().__init__(age_limit=5)

    def eat(self, food_type):
        if food_type == "Rabbit":
            print("Fox eat Rabbit")
        else:
            print("Fox doesn't eat Rabbit")


class Rabbit(Living):
    def __init__(self):
        super().__init__(age_limit=3)

    def eat(self, food_type):
        if food_type == "Plant":
            print("Rabbit eat Plant")
        else:
            print("Rabbit doesn't eat Plant")


class Plant(Living):
    def __init__(self):
        super().__init__(age_limit=10)

    def eat(self, food_type):
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