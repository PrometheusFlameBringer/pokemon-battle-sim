from pokemon import Pokemon, Move
from battle import Stage
from display import Displayer
from api_connect import MoveStats

team1 = [Pokemon("Red", "Charmander", 100),Pokemon("Green", "Rowlet", 100)]
team2 = [Pokemon("Blue", "Squirtle", 100)]


#Team 1: Charmander
team1[0].add_move("Ember")
team1[0].add_move("Scratch")

team1[1].add_move("Leafage")
team1[1].add_move("Tackle")

#Team 2: Squirtle
team2[0].add_move("Bubble")
team2[0].add_move("Tackle")

#battle = Stage(team1, team2)
#Displayer(battle)
