from poke_stats import PokeStats

VALID_TYPES = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

class Pokemon:
    def __init__(self, name, species, level, type1, type2=None, moves=None):
        self.name = name
        self.species = species
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.stats = PokeStats()
        self.currHP = 0
        self.moves = moves if moves is not None else []

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
    
    def set_stats(self, stats = None):
        if stats:
            for stat, value in stats.items():
                getattr(self.stats, f"set_{stat}")(value)
        else:
            self.rotate_stat("set_")

    def get_stats(self):
        self.rotate_stat("get_")
    
    def get_stat(self, stat=""):
        return getattr(self.stats, "get_" + self.stat_check(stat))()

    def set_stat(self, stat=None, value=None):
        if stat is None:
            stat = self.stat_check()
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
        return self.stats.get_HP()

    def get_moves(self):
        return self.moves

    def full_heal(self):
        self.currHP = self.stats.get_HP()

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
    
    def stat_check(self, stat= ""):
        while True:
            if stat == "":
                stat = input("Enter stat: ")

            if stat in ["HP", "Atk", "Def", "SpAtk", "SpDef", "Spd"]:
                break

            print("Invalid input please try again")
            stat = input("Enter stat: ")
        return stat

class Move:
    def __init__(self, 
                 name:str, 
                 poke_type:str, 
                 physical:bool, 
                 power:int, 
                 accuracy:int, 
                 pp:int, 
                 priority:int,
                 user:Pokemon,
                 target:Pokemon = None):
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
