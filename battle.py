from damage import Damage
import random

class Stage:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.calculator = None
        self.move_queue = []
        self.moves_list = {}

    def use_move(self, move):
        attacker, defender = move.get_user(), move.get_target()
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

    def add_move(self,move,pokeSpeed, target):
        move.set_target(target)
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
    
    def set_queue(self, moves = None):
        prio = list(moves.keys()) if moves else list(self.moves_list.keys())
        prio.sort(reverse=True)
        out = []
        
        for i in prio:
            if moves:
                out.append(moves[i])
                continue
            
            for j in self.set_queue(self.moves_list[i]):
                self.move_queue.append(j)
        
        return out

    def use_queue(self):
        self.set_queue()
