import random


class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive=True
        self.ammo=5
        self.armor=60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        tanques.remove(self)
        print(self.name, "explodes!")


tanques = [Tank("Bob"), Tank("Jack"), Tank("Roger"), Tank("Trust"), Tank("Liberty")]

while len(tanques) > 1:
    tanqueAtacante = random.choice(tanques)
    tanquesAtacados = [item for item in tanques if item != tanqueAtacante]
    tanqueAtacado = random.choice(tanquesAtacados)
    tanqueAtacante.fire_at(tanqueAtacado)
    print(f"{tanqueAtacante.name} atacou o {tanqueAtacado.name} deixando ele com armor = {tanqueAtacado.armor}")

print(f"O vencedor foi {tanques[0]}")