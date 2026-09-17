from typechart import TypeChart
import random

class Damage:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender
        self.typeChart = TypeChart()

    def calculate_damage(self, move, other = 1):
        #Declare values
        level = self.attacker.level
        power = move.power
        attack = self.attacker.stats.get_Atk() if move.physical == "Physical" else self.attacker.stats.get_SpAtk()
        defense = self.defender.stats.get_Def() if move.physical == "Physical" else self.defender.stats.get_SpDef()

        #Main formula
        damage = (((((2*level)//5)+ 2) * power * (attack/defense))//50) + 2

        #Modifiers
        #Random Factor
        random_factor = random.randint(85, 100) / 100
        modifier = random_factor

        #Critical Hit 
        critical = random.randint(1, 24)
        if critical == 24:
            modifier *= 1.5

        #Type Effectiveness
        modifier *= self.typeChart.get_effectiveness(self.defender.type1, move.poke_type) 
        if self.defender.type2:
            modifier *= self.typeChart.get_effectiveness(self.defender.type2, move.poke_type)

        #STAB
        if move.poke_type == self.attacker.type1 or move.poke_type == self.attacker.type2:
            modifier *= 1.5

        #Other Modifiers
        modifier *= other
        return round(damage * modifier)
