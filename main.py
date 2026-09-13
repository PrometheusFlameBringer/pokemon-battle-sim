from pokemon import Pokemon
from move import Move
from battle import Stage
import os

team1 = [Pokemon("Red", "Charmander", 100, "Fire")]
team2 = [Pokemon("Blue", "Squirtle", 100, "Water")]

#Team 1: Charmander
team1[0].set_stats({
    "HP": 219, 
    "Atk": 140, 
    "Def": 122, 
    "SpAtk": 156, 
    "SpDef": 136, 
    "Spd": 166})
team1[0].add_move(Move("Ember", "Fire", False, 40, 100, 25, 0))
team1[0].add_move(Move("Scratch", "Normal", True, 40, 100, 35, 0))

#Team 2: Squirtle
team2[0].set_stats({
    "HP": 229, 
    "Atk": 132, 
    "Def": 166, 
    "SpAtk": 136, 
    "SpDef": 164, 
    "Spd": 122})
team1[1].add_move(Move("Bubble", "Water", False, 40, 100, 25, 0))
team1[1].add_move(Move("Scratch", "Normal", True, 40, 100, 35, 0))

battle = Stage(team1, team2)
starting=battle.battle_start()
for i in starting:
    i.full_heal()

os.system('cls' if os.name == 'nt' else 'clear')
input("Battle Start!\nPress Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')
print(f"\t\t\t{starting[1].species}\n\t\t\t{starting[1].currHP}/{starting[1].get_maxHP()}\n\n\n{starting[0].name}\n{starting[0].currHP}/{starting[0].get_maxHP()}\n")
moves = starting[0].get_moves()
[print(f"{i+1}) {moves[i].name} | {moves[i].pp}") for i in range(len(moves))]