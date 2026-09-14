from pokemon import Pokemon
from move import Move
from battle import Stage
from display import Displayer

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
team2[0].add_move(Move("Bubble", "Water", False, 40, 100, 25, 0))
team2[0].add_move(Move("Scratch", "Normal", True, 40, 100, 35, 0))

battle = Stage(team1, team2)
Displayer(battle)