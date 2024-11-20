from random import randint

class Animal: # общий класс животное
    live = True
    sound = None # звук
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self, speed: int):
        self._cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed # скорость передвижения существа

    def move(self, dx: int, dy: int, dz: int):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you O_O")

    def speak(self):
        print(self.sound)

class Bird(Animal): # птицы
    beak = True # наличие клюва

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")

class AquaticAnimal(Animal): # плавающие животные
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz: int):
        self._cords[2] -= int(abs(dz) * (self.speed / 2))

class PoisonousAnimal(Animal): # ядовитые животные
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal): # утконос
    sound = "Click-click-click" # звук утконоса



db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
