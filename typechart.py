class TypeChart:
    def __init__(self):
        self.types = {
            "fire":{"water":2, "grass":0.5},
            "water":{"fire":0.5, "grass":2},
            "grass":{"fire":2, "water":0.5},
            "normal":{}
        }

    def get_effectiveness(self, target_type, move_type):
        return self.types.get(target_type, {}).get(move_type, 1)