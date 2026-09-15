VALID_TYPES = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

class Move:
    def __init__(self, name:str, poke_type:str, physical:bool, power:int, accuracy:int, pp:int, priority:int):
        if poke_type not in VALID_TYPES:
            raise ValueError(f"{poke_type} is an invalid Pokemon type.")
        
        self.name = name
        self.poke_type = poke_type
        self.physical = physical
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    def get_poke_type(self):
        return self.poke_type

    def set_poke_type(self, x):
        self.poke_type = x

    def get_physical(self):
        return self.physical

    def set_physical(self, x):
        self.physical = x

    def get_power(self):
        return self.power

    def set_power(self, x):
        self.power = x

    def get_accuracy(self):
        return self.accuracy

    def set_accuracy(self, x):
        self.accuracy = x

    def get_pp(self):
        return self.pp

    def set_pp(self, x):
        self.pp = x

    def get_priority(self):
        return self.priority

    def set_priority(self, x):
        self.priority = x
