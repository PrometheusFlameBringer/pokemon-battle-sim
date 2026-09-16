from damage import Damage
import random

class Stage:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.calculator = None
        self.move_queue = []
        self.moves_list = {}

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

    def add_move(self,move,pokeSpeed):
        prio = move.get_priority()

        if prio not in list(self.moves_list.keys()):
            self.moves_list[prio] = {pokeSpeed:[move]}
            return

        x = self.moves_list[prio]
        if pokeSpeed not in list(x.keys()):
            x[pokeSpeed] = [move]
            return

        x[pokeSpeed].append(move)
        return

    def set_queue(self):
        prio=list(self.moves_list.keys())
        prio.sort(reverse=True)
        
        for i in prio:
            for j in self.set_queue_speed(self.moves_list[i]):
                self.move_queue.append(j[0].name)
        
    def set_queue_speed(self, moves):
        speeds = list(moves.keys())
        speeds.sort(reverse=True)
        out = []
        
        for i in speeds:
            out.append(moves[i])
        
        return out
