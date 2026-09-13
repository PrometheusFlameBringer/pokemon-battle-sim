class PokeStats:
    def __init__(self):
        self.HP = 10
        self.Atk = 10
        self.Def = 10
        self.SpAtk = 10
        self.SpDef = 10
        self.Spd = 10

    def set_HP(self, HP):
        self.HP = HP

    def set_Atk(self, Atk):
        self.Atk = Atk
        
    def set_Def(self, Def):
        self.Def = Def
        
    def set_SpAtk(self, SpAtk):
        self.SpAtk = SpAtk

    def set_SpDef(self, SpDef):
        self.SpDef = SpDef
        
    def set_Spd(self, Spd):
        self.Spd = Spd

    def get_HP(self):
        return self.HP

    def get_Atk(self):
        return self.Atk
        
    def get_Def(self):
        return self.Def
        
    def get_SpAtk(self):
        return self.SpAtk

    def get_SpDef(self):
        return self.SpDef
        
    def get_Spd(self):
        return self.Spd
    