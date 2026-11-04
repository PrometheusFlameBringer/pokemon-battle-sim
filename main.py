from pokemon import Pokemon, Move
from battle import Stage
from display import Displayer

team1 = [Pokemon("Red", "Charmander", 100),Pokemon("Green", "Bulbasaur", 100)]
team2 = [Pokemon("Blue", "Squirtle", 100)]

#Team 1: Charmander
team1[0].add_move(Move("Ember", "Fire", "Special", 40, 100, 25, 0, team1[0]))
team1[0].add_move(Move("Scratch", "Normal", "Physical", 40, 100, 35, 0, team1[0]))

team1[1].add_move(Move("Leafage", "Grass", "Physical", 40, 100, 25, 0, team1[0]))
team1[1].add_move(Move("Scratch", "Normal", "Physical", 40, 100, 35, 0, team1[0]))

#Team 2: Squirtle
team2[0].add_move(Move("Bubble", "Water", "Special", 40, 100, 25, 0, team2[0]))
team2[0].add_move(Move("Scratch", "Normal", "Physical", 40, 100, 35, 0, team2[0]))

battle = Stage(team1, team2)
Displayer(battle)