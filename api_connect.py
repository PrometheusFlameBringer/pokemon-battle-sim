import requests, os, json

class PokemonBase:
    def __init__(self,species:str):
        self.species = species
        self.data = None
        self.battleset = None
        self.backup()
        self.connect()

    def backup(self):
        filename = "battle.json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.battleset = json.load(f)
        else:
            self.battleset = {}
            with open(filename, "w") as f:
                json.dump(self.battleset, f)

    def save(self):
        filename = "battle.json"
        with open(filename, "w") as f:
            json.dump(self.battleset, f)

    def connect(self):
        if self.species.lower() in self.battleset:
            self.data = self.battleset[self.species.lower()]
            return
        url = f"https://pokeapi.co/api/v2/pokemon/{self.species.lower()}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            self.data = response.json()
            self.battleset[self.species.lower()] = {
                'stats':{stat['stat']['name']: stat['base_stat'] for stat in self.data['stats']},
                'types':[i['type']['name'] for i in self.data['types']],
                'ablities':[{i['ability']['name']:{'is_hidden':i['is_hidden'],'id':i['ability']['url'].split('/')[-2]}} for i in self.data['abilities']],
                'moves':{i['move']['name']:i['move']['url'].split('/')[-2] for i in self.data['moves']}}
            self.save()
        else:
            raise Exception(f"Failed to fetch data for {self.species}. Status code: {response.status_code}")

    def get_base_stats(self):
        if self.data:
            return self.data["stats"]
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
        return self.data["types"]
