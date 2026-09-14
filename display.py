import os

class Displayer:
    def __init__(self, stage, heal = True):
        self.stage = stage
        self.heal = heal
        self.pokeX = None
        self.pokeY = None

        self.start_game()

    def start_game(self):
        if self.heal:
            self.stage.heal_all()

        self.pokeX, self.pokeY = self.stage.get_start()

        self.get_state()
        self.list_moves()

    def get_state(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\t\t\t{self.pokeY.species}\n\t\t\t{self.pokeY.currHP}/{self.pokeY.get_maxHP()}\n\n\n{self.pokeX.name}\n{self.pokeX.currHP}/{self.pokeX.get_maxHP()}\n")

    def list_moves(self):
        moves = self.pokeX.get_moves()
        [print(f"{i+1}) {moves[i].name} | {moves[i].pp}") for i in range(len(moves))]
        input("\nEnter move to use: ")