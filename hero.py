import random
from ability import Ability
from armor import Armor

# heroes = ["Wonder Woman", "Dumbledore", "Spiderman", "Batman", "Captain Planet", "Ant Man"]

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.abilities = []
        self.armors = []

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

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        '''add armor to armor list which is self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''calculate the total block amount from all armor blocks
        return: total_block:Int
        '''
        total_block = 0
        if self.armors:
            
            for armor in self.armors:
                total_block += armor.block()
                
        # if self.current_health <= 0:
        #     total_block = 0
        return total_block
        
        

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health -= (damage - self.defend())
        # self.current_health -= self.defend(damage)

        return self.current_health
        # stretch:  maybe have damage as a negative number?
    
    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else:
            return True



        
        
if __name__ == "__main__":

    my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")

    # hero1.fight(hero2)

    # ability1 = Ability("Great Debugging", 50)
    # ability2 = Ability("Blue-Light vision", 90)
    # my_hero.add_ability(ability1)
    # my_hero.add_ability(ability2)
    # print(my_hero.abilities)
    # print(my_hero.attack())

    # armor1 = Armor("Shield", 100)
    # armor2 = Armor("Helmet", 60)
    # my_hero.add_armor(armor1)
    # my_hero.add_armor(armor2)
    # print(my_hero.armors)
    # print(my_hero.defend())
    # my_hero.take_damage(50)
    # print(my_hero.current_health)
    my_hero.take_damage(150)
    print(my_hero.is_alive())
    my_hero.take_damage(15000)
    print(my_hero.is_alive())
