from poke_stats import PokeStats

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
