from damage import Damage
import random

class Stage:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.calculator = Damage(self.team1[0], self.team2[0])

    def use_move(self, move, attacker, defender):
        if move.accuracy >= 100:
            acc_check = random.randint(1, 100)
            if acc_check < move.accuracy:
                return f"{attacker.name}'s {move.name} missed!"

        damage = self.calculator.calculate_damage(move)

        return f"{defender.name} took {damage} damage!"

    def battle_start(self):
        return [self.team1[0], self.team2[0]]