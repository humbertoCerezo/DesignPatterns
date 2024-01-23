import copy

class npc():
    def __init__(self):
        self.name = None
        self.gender = None

    def __str__(self):
        return f"Nombre: {self.name} Género: {self.gender}"
    
    def clone(self):
        return copy.deepcopy(self)
    

class enemy():
    def __init__(self):
        self.name = None
        self.damage = None
        self.weapon = None

    def __str__(self):
        return f"Nombre: {self.name} Daño: {self.damage} Arma: {self.weapon}"
    
    def clone(self):
        return copy.deepcopy(self)
    

#EJEMPLO DE LA CLASE NPC
originalNpc = npc()
originalNpc.name = "Personaje Original"
originalNpc.gender = "Male"

print(f"NPC Original: {originalNpc}")

cloneNpc = originalNpc.clone()
cloneNpc.name = "Personaje Clonado"
cloneNpc.gender = "Female"

print(f"NPC CLONADO: {cloneNpc}")

#EJEMPLO CON LA CLASE ENEMY

slime = enemy()
slime.name = "Slime"
slime.damage = 15
slime.weapon = "None"

print(f"PrimerEnemigo: {slime}")

slimeBoss = slime.clone()
slimeBoss.name = "Slime Boss"
slimeBoss.damage = 30
slimeBoss.weapon = "None"

print(f"SLIME BOSS: {slimeBoss}")