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