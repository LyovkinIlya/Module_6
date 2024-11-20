class Animal:
    alive = True # живой
    fed = False # накормленный

    def __init__(self, name: str):
        self.name = name

    def __repr__(self): # для правильного отображения в консоли, если в food передать объект Animal
        return self.name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                Animal.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                Animal.alive = False
        else:
            print(f"{food} должен быть объектом класса Fruit или Flower")

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    edible = False # съедобность

    def __init__(self, name: str):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True # съедобность

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
a2.eat(a1)
a2.eat("Стр")