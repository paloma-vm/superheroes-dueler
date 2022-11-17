import random

# heroes = ["Wonder Woman", "Dumbledore", "Spiderman", "Batman", "Captain Planet", "Ant Man"]

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
            # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        #                      ^^^^^^^^^^
    
    def fight(self, opponent):
        '''Current hero will take turns fighting the opponent hero passed in'''
          # TODO: Fight each hero until a victor emerges.
            # Phases to implement:
            #1) randomly choose winner,
            # Hint: Look into random library, more specifically the choice method
        fighters = [self.name, opponent.name]#!!!
        victor = random.choice(fighters)
        print(f"{victor} wins!")
    




if __name__ == "__main__":

    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)