import random

class Warrior:
    def __init__(self, name, health, damage, x, y):
        self.name = name
        self.health = health
        self.damage = damage
        self.x = x
        self.y = y

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} ({self.health} hp)"


class Battle:
    def __init__(self, field_size):
        self.field = [[None for _ in range(field_size)] for _ in range(field_size)]
        self.field_size = field_size

    def add_warrior(self, warrior):
        self.field[warrior.x][warrior.y] = warrior

    def remove_warrior(self, warrior):
        self.field[warrior.x][warrior.y] = None

    def move_warrior(self, warrior, x, y):
        if self.field[x][y] is not None:
            return False
        self.remove_warrior(warrior)
        warrior.x = x
        warrior.y = y
        self.add_warrior(warrior)
        return True

    def is_adjacent(self, x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

    def perform_battle(self, warrior1, warrior2):
        print(f"{warrior1} vs {warrior2}")
        while warrior1.is_alive() and warrior2.is_alive():
            warrior2.health -= warrior1.damage
            if warrior2.is_alive():
                warrior1.health -= warrior2.damage
            print(f"{warrior1} vs {warrior2}")
        if not warrior1.is_alive():
            print(f"{warrior1} погиб")
        if not warrior2.is_alive():
            print(f"{warrior2} погиб")

    def perform_multiple_battles(self, warriors):
        while len(warriors) > 1:
            random.shuffle(warriors)
            for i in range(0, len(warriors), 2):
                if i+1 < len(warriors):
                    warrior1 = warriors[i]
                    warrior2 = warriors[i+1]
                    if self.is_adjacent(warrior1.x, warrior1.y, warrior2.x, warrior2.y):
                        self.perform_battle(warrior1, warrior2)
                        if not warrior1.is_alive():
                            warriors.remove(warrior1)
                        if not warrior2.is_alive():
                            warriors.remove(warrior2)
                    else:
                        x = random.randint(0, len(self.field)-1)
                        y = random.randint(0, len(self.field[0])-1)
                        self.move_warrior(warrior1, x, y)
                        x = random.randint(0, len(self.field)-1)
                        y = random.randint(0, len(self.field[0])-1)
                        self.move_warrior(warrior2, x, y)
        print(f"Победитель: {warriors[0].name}")


# Создаем поле и добавляем войнов
field_size = 10
battle = Battle(field_size)
warriors = [Warrior("Воин 1", 100, 10, 2, 2),
            Warrior("Воин 2", 100, 10, 8, 8),
            Warrior("Воин 3", 100, 10, 4, 4),
            Warrior("Воин 4", 100, 10, 5, 5),
            Warrior("Воин 5", 100, 10, 1, 9),
            Warrior("Воин 6", 100, 10, 9, 1),
            Warrior("Воин 7", 100, 10, 1, 1),
            Warrior("Воин 8", 100, 10, 9, 9),]

for warrior in warriors:
    battle.add_warrior(warrior)

while len(warriors) > 1:
    battle.perform_multiple_battles(warriors)

print(f"Победитель: {warriors[0].name}")