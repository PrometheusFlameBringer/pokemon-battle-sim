import requests

class PokemonBase:
    def __init__(self,species:str):
        self.species = species
        self.data = None
        self.connect()

    def connect(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.species.lower()}/"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            raise Exception(f"Failed to fetch data for {self.species}. Status code: {response.status_code}")

    def get_base_stats(self):
        if self.data:
            stats = {stat['stat']['name']: stat['base_stat'] for stat in self.data['stats']}
            return stats
        else:
            raise Exception("No data available. Please connect first.")

    def set_stats(self,EVs={},lvl=1):
        if not self.data:
            raise Exception("No data available. Please connect first.")

        calculated_stats = {}
        for stat, base_value in self.get_base_stats().items():  
            ev = EVs.get(stat, 0)
            iv = 31
            calced_stat = (((2 * base_value + iv + (ev // 4)) * lvl) // 100) + ((lvl + 10) if stat == "hp" else 5)
            calculated_stats[stat] = calced_stat
        return calculated_stats

print(PokemonBase("Charmander").set_stats(lvl = 5))