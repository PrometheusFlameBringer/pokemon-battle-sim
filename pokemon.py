from poke_stats import PokeStats
from poke import PokemonBase

VALID_TYPES = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

class Pokemon:
    def __init__(self, name, species, level, moves=None):
        self.name = name
        self.species = PokemonBase(species)
        self.level = level
        self.type1 = None
        self.type2 = None
        self.stats = PokeStats()
        self.currHP = 0
        self.moves = moves if moves is not None else []
        
    #Set base from species
    def set_base(self):
        self.set_stats()
        self.set_types()

    def set_types(self):
        types = self.species.get_types()
        if len(types)>1:
            self.type2 = types[1]
        self.type1 = types[0]

    #Stats
    def rotate_stat(self, prefix):
        statKeys = list(self.stats.__dict__.keys())

        for i in statKeys:
            methodName = prefix + i
            method = getattr(self.stats, methodName)

            if prefix == "set_":
                method(self.num_check(i))
                continue
            if prefix == "get_":
                print(method())
                continue
    
    def set_stats(self, EVs=None):
        if EVs is None:
            EVs = {stat: 0 for stat in self.stats.__dict__.keys()}

        cur_stats = self.species.set_stats(EVs, self.level)
        for stat, value in cur_stats.items():
            self.set_stat(stat, value)

    def get_stats(self):
        self.rotate_stat("get_")
    
    def get_stat(self, stat=""):
        return getattr(self.stats, "get_" + self.stat_check(stat))()

    def set_stat(self, stat=None, value=None):
        stat = self.stat_check(stat)
        
        if value is None:
            value = self.num_check(stat)
        getattr(self.stats, "set_" + stat)(value)

    #Moves
    def add_move(self, move):
        if len(self.moves) < 4:
            self.moves.append(move)
        else:
            print("Cannot add more than 4 moves.")

    def get_move(self, i):
        return self.moves[i]

    #Battle
    def get_currHP(self):
        return self.currHP

    def get_maxHP(self):
        return self.stats.get_hp()

    def get_moves(self):
        return self.moves

    def full_heal(self):
        self.currHP = self.stats.get_hp()

    def dmg (self, damage):
        self.currHP -= damage
        if self.currHP < 0:
            self.currHP = 0

    #Error Handling
    def num_check(self, i):
            out = 0
            while True:
                try:
                    out = int(input(f"Enter value for {i}: "))
                except:
                    print("Invalid input please try again")
                else:
                    break
            return out
    
    def stat_check(self, stat=None):
        if stat:
            return stat.replace("-","_")
        stat = ""
        while True:
            if stat == "":
                stat = input("Enter stat: ")

            if stat in ["HP", "Atk", "Def", "SpAtk", "SpDef", "Spd"]:
                break

            print("Invalid input please try again")
            stat = input("Enter stat: ")
        return stat

    
    
class Move:
    def __init__(self, name:str, poke_type:str, physical:str, power:int, accuracy:int, pp:int, priority:int,user:Pokemon, target:Pokemon = None):
        if poke_type not in VALID_TYPES:
            raise ValueError(f"{poke_type} is an invalid Pokemon type.")
        
        self.name = name
        self.poke_type = poke_type
        self.physical = physical
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority
        self.user = user
        self.target = target

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

    def get_user(self):
        return self.user

    def set_user(self, x):
        self.user = x

    def get_target(self):
        return self.target

    def set_target(self, x):
        self.target = x
    