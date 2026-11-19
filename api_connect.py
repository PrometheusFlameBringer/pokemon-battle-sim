import requests, os, json

class PokemonBase:
    def __init__(self,species:str):
        self.species = species.lower()
        self.battleset = {}
        self.moveset = {}
        self.abilityset = {}
        self.spriteset = {}
        self.backup()
        self.connect()

    def backup(self):        
        self.battleset = self.set_file("pokemon_base.json")
        self.moveset = self.set_file("moves_base.json")
        self.abilityset = self.set_file("abilities_base.json")
        self.spriteset = self.set_file("sprites_base.json")
    
    def set_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return json.load(f)
        else:
            with open(filename, "w") as f:
                json.dump({}, f)
            return {}

    def save(self,filename,info):
        with open(filename, "w") as f:
            json.dump(info, f)

    def set_vars(self):
        self.battleset = self.battleset[self.species]
        self.moveset = self.moveset[self.species]
        self.abilityset = self.abilityset[self.species]
        self.spriteset = self.spriteset[self.species]

    def connect(self):
        if self.species in self.battleset:
            self.set_vars()
            return

        #If not found
        url = f"https://pokeapi.co/api/v2/pokemon/{self.species}/"

        try:
            response = requests.get(url)
        except:
            print("fail")
        
        if response.status_code == 200:
            data = response.json()
            self.battleset[self.species], self.moveset[self.species], self.abilityset[self.species], self.spriteset[self.species] = {'stats':{stat['stat']['name']: stat['base_stat'] for stat in data['stats']}, 'types':[i['type']['name'] for i in data['types']]}, {i['move']['name']:i['move']['url'].split('/')[-2] for i in data['moves']}, [{i['ability']['name']:{'is_hidden':i['is_hidden'],'id':i['ability']['url'].split('/')[-2]}} for i in data['abilities']], {"front_default":data['sprites']["front_default"],"front_shiny":data['sprites']["front_shiny"],"back_default":data['sprites']["back_default"],"back_shiny":data['sprites']["back_default"]}
            
            for i,j in {"pokemon_base.json":self.battleset,"moves_base.json":self.moveset,"abilities_base.json":self.abilityset,"sprites_base.json":self.spriteset}.items():
                self.save(i,j)
        else:
            raise Exception(f"Failed to fetch data for {self.species}. Status code: {response.status_code}")
        
        self.set_vars()

    def get_move_list(self):
        return self.moveset.keys()

    def get_move_id(self, move_name):
        return self.moveset.get(move_name, 'eme')

    def get_base_stats(self):
        if self.battleset:
            return self.battleset["stats"]
        else:
            raise Exception("No data available. Please connect first.")

    def set_stats(self,EVs={},lvl=1):
        if not self.battleset:
            raise Exception("No data available. Please connect first.")

        calculated_stats = {}
        for stat, base_value in self.get_base_stats().items():  
            ev = EVs.get(stat, 0)
            iv = 31
            calced_stat = (((2 * base_value + iv + (ev // 4)) * lvl) // 100) + ((lvl + 10) if stat == "hp" else 5)
            calculated_stats[stat] = calced_stat
        return calculated_stats

    def get_types(self):
        return self.battleset["types"]

class MoveStats:
    def __init__(self, move:str, user):
        self.move = move.lower()
        self.moveset = None
        if self.valid_user(user):
            self.backup()
            self.connect()

    def backup(self):
            filename = "moves.json"
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    self.moveset = json.load(f)
            else:
                self.moveset = {}
                with open(filename, "w") as f:
                    json.dump(self.moveset, f)

    def save(self):
        filename = "moves.json"
        with open(filename, "w") as f:
            json.dump(self.moveset, f)

    def connect(self):
        if self.move in self.moveset:
            self.moveset = self.moveset[self.move]
            return
        
        url = f"https://pokeapi.co/api/v2/move/{self.move}/"
        
        try:
            response = requests.get(url)
        except:
            print("fail")

        if response.status_code == 200:
            data = response.json()
            self.move = data['name']
            self.moveset[data['name']] = {
                'type': data['type']['name'],
                'damage_class': data['damage_class']['name'],
                'power': data['power'],
                'accuracy': data['accuracy'],
                'pp': data['pp'],
                'priority': data['priority'],
                'description': self.get_move_desc(data['flavor_text_entries'])
            }
            self.save()
        else:
            raise Exception(f"Failed to fetch data for move {self.move}. Status code: {response.status_code}")
        self.moveset = self.moveset[self.move]
    
    def valid_user(self, user):
        if self.move in user.species.get_move_list():
            return True
        return False

    def get_move_data(self):
        info = self.moveset
        return info['type'], info['damage_class'], info['power'], info['accuracy'], info['pp'], info['priority']

    def get_move_desc(self, entries):
        for i in entries:
            if i['language']['name'] == 'en':
                return i['flavor_text']
