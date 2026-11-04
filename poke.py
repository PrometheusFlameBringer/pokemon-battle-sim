import requests, os, json

class PokemonBase:
    def __init__(self,species:str):
        self.species = species
        self.data = None
        self.dataset = None
        self.backup()
        self.connect()

    def backup(self):
        filename = "dataset.json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.dataset = json.load(f)
        else:
            self.dataset = {}
            with open(filename, "w") as f:
                json.dump(self.dataset, f)

    def save(self):
        filename = "dataset.json"
        with open(filename, "w") as f:
            json.dump(self.dataset, f)

    def connect(self):
        if self.species.lower() in self.dataset:
            self.data = self.dataset[self.species.lower()]
            return
        print(self.species.lower())
        url = f"https://pokeapi.co/api/v2/pokemon/{self.species.lower()}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            self.data = response.json()
            self.dataset[self.species.lower()] = self.data
            self.save()
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

    def get_types(self):
        return [i['type']['name'] for i in self.data["types"]]