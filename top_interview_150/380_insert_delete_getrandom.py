from random import choice

class RandomizedSet:

    def __init__(self):
        self.h_map = {}

    def insert(self, val: int) -> bool:
        if val in self.h_map:
            return False
        else:
            self.h_map[val] = True
            return True

    def remove(self, val: int) -> bool:
        return self.h_map.pop(val, False)

    def getRandom(self) -> int:
        return choice(list(self.h_map))

