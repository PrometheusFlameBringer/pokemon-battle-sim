class PokeStats:
    def __init__(self):
        self.hp = 10
        self.attack = 10
        self.defense = 10
        self.special_attack = 10
        self.special_defense = 10
        self.speed = 10

    def set_hp(self, hp):
        self.hp = hp

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_special_attack(self, special_attack):
        self.special_attack = special_attack

    def set_special_defense(self, special_defense):
        self.special_defense = special_defense

    def set_speed(self, speed):
        self.speed = speed

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense
        
    def get_special_attack(self):
        return self.special_attack

    def get_special_defense(self):
        return self.special_defense
        
    def get_speed(self):
        return self.speed
    