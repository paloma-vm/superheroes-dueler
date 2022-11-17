import random

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.'''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Return a value between 0 and the value set by self.max_block.'''
        random_value = random.randint(0, self.max_block)
        return random_value

if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())