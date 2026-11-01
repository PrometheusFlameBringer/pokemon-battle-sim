class PokeStats:
    def __init__(self):
        self.HP = 10
        self.Atk = 10
        self.Def = 10
        self.SpAtk = 10
        self.SpDef = 10
        self.Spd = 10

    def set_hp(self, HP):
        self.HP = HP

    def set_attack(self, Atk):
        self.Atk = Atk
        
    def set_defense(self, Def):
        self.Def = Def
        
    def set_special_attack(self, SpAtk):
        self.SpAtk = SpAtk

    def set_special_defense(self, SpDef):
        self.SpDef = SpDef
        
    def set_speed(self, Spd):
        self.Spd = Spd

    def get_hp(self):
        return self.HP

    def get_attack(self):
        return self.Atk
        
    def get_defense(self):
        return self.Def
        
    def get_special_attack(self):
        return self.SpAtk

    def get_special_defense(self):
        return self.SpDef
        
    def get_speed(self):
        return self.Spd
    