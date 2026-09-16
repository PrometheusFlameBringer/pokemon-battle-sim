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

        self.pokeY, self.pokeX = self.stage.get_start()

        while True:
            for i in range(2):
                self.rotation()

            print(self.stage.moves_list)
            break
            
            if self.pokeX.get_currHP() == 0 or self.pokeY.get_currHP() == 0:
                break

    def rotation(self,message=None):
        self.switch_poke()
        self.get_state(message)

    def get_state(self,message):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\t\t\t{self.pokeY.species}\n\t\t\t{self.pokeY.currHP}/{self.pokeY.get_maxHP()}\n\n\n{self.pokeX.name}\n{self.pokeX.currHP}/{self.pokeX.get_maxHP()}\n")

        if message:
            print(message)
            return
        self.list_moves()

    def list_moves(self):
        moves = self.pokeX.get_moves()
        [print(f"{i+1}) {moves[i].name} | {moves[i].pp}") for i in range(len(moves))]

        try:
            x = int(input("\nEnter move to use: "))
            if x > len(moves) or x < 1:
                raise ValueError()
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            input("Invalid input please enter the number of the move.\nPress enter to continue...")
            self.get_state()
        else:
            self.move(x-1)

    def move(self, moveNum):
        move = self.pokeX.get_move(moveNum)
        self.stage.add_move(move,self.pokeX.get_stat("Spd"))
        input(self.stage.use_move(move, self.pokeX, self.pokeY))

    def switch_poke(self):
        self.pokeX, self.pokeY = self.pokeY, self.pokeX