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

            self.use_queue()
            
            if self.pokeX.get_currHP() == 0 or self.pokeY.get_currHP() == 0:
                break

    def use_queue(self):
        self.stage.set_queue()
        queue = self.stage.move_queue

        for i in queue:
            pokeMove = i[0]
            self.rotation(f"{pokeMove.user.name} used {pokeMove.name}")
            self.get_state(self.stage.use_move(pokeMove))

        self.stage.move_queue.clear()
        self.stage.moves_list.clear()

    def rotation(self,message=None):
        self.switch_poke()
        self.get_state(message)

    def get_state(self,message):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\t\t\t{self.pokeY.species}\n\t\t\t{self.pokeY.currHP}/{self.pokeY.get_maxHP()}\n\n\n{self.pokeX.name}\n{self.pokeX.currHP}/{self.pokeX.get_maxHP()}\n")

        if message:
            print(message)
            input("Press enter to continue...")
            return
        self.list_moves()
        input("Press enter to continue...")

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
        self.stage.add_move(move,self.pokeX.get_stat("Spd"), self.pokeY)

    def switch_poke(self):
        self.pokeX, self.pokeY = self.pokeY, self.pokeX
