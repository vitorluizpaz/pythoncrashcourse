from random import randint

class Dice():
    def __init__(self, sides):
        self.sides = sides
    def roll_die(self):
        number = randint(1, self.sides)
        print(number)

dice1 = Dice(6)
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
