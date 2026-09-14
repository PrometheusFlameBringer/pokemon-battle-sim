from damage import Damage
import random

class Stage:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.calculator = None

    def use_move(self, move, attacker, defender):
        self.calculator = Damage(attacker, defender)

        if move.accuracy >= 100:
            acc_check = random.randint(1, 100)
            if acc_check > move.accuracy:
                return f"{attacker.name}'s {move.name} missed!"

        damage = self.calculator.calculate_damage(move)

        return f"{defender.species} took {damage} damage!"

    def team_heal(self, team):
        for i in team:
            i.full_heal()

    def heal_all(self):
        self.team_heal(self.team1)
        self.team_heal(self.team2)

    def get_alive(self,team):
        for i in team:
            if i.currHP > 0:
                return i

        return -1

    def get_start(self):
        return self.get_alive(self.team1),self.get_alive(self.team2)