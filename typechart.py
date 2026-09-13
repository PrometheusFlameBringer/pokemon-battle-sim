class TypeChart:
    def __init__(self):
        self.types = {
            "Fire":{"Water":2, "Grass":0.5},
            "Water":{"Fire":0.5, "Grass":2},
            "Grass":{"Fire":2, "Water":0.5},
            "Normal":{}
        }

    def get_effectiveness(self, target_type, move_type):
        return self.types.get(target_type, {}).get(move_type, 1)