
###
class BrawlhallaCharacter:
    def __init__(self, name, weapon1, weapon2, strength, dexterity, defense, speed):
        self.name = name
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.stats = {
            'strength': strength,
            'dexterity': dexterity,
            'defense': defense,
            'speed': speed

        }
    def display_stats(self):
        print(f"---{self.name}---")
        print(f"Weapons: {self.weapon1} & {self.weapon2}")
    def enhance_stat(self, increase_stat, decrease_stat):
        if increase_stat not in self.stats or decrease_stat not in self.stats:
            print('Invalid stat name')
            return False
        if self.stats[decrease_stat] <= 0:
            print(f"{decrease_stat} is finished")
            return False
        
        self.stats[increase_stat] += 1
        self.stats[decrease_stat] -= 1
        print(f'{self.name} increased {increase_stat} by 1 and decreased {decrease_stat} by 1')
        return True

class Nix(BrawlhallaCharacter):
    def __init__(self):
        super().__init__('Nix', 'Scythe', 'Blasters', 5, 6, 6, 5)

    def special_move(self):
        print(f"{self.name} uses Shadow Strike")

class Bodvar(BrawlhallaCharacter):
    def __init__(self):
        super().__init__('Bodvar', 'Sword', 'Hammer', 6, 5, 6, 5)

    def special_move(self):
        print(f"{self.name} uses Odin's smash")

class Ember(BrawlhallaCharacter):
    def __init__(self):
        super().__init__('Ember', 'Bow', 'Katars', 6, 7, 3, 6)

    def special_move(self):
        print(f"{self.name} uses Wolf Arrow")

class Orion(BrawlhallaCharacter):
    def __init__(self):
        super().__init__('Orion', 'Spear', 'Lance', 6, 4, 7, 5)

    def special_move(self):
        print(f"{self.name} uses Cosmic Blast")

def interface(character):
    while True:
        character.display_stats()
        print("Enter 'q' to quit")
        increase = input('Which stat do you want to increase? ').lower()
        if increase == 'q':
            break
        decrease = input('Which stat do you want to decrease? ').lower()
        if decrease == 'q':
            break
        character.enhance_stat(increase, decrease)

characters = [Nix(), Bodvar(), Ember(), Orion()]

print('Choose a character by number:')
for i, c in enumerate(characters, start=1):
    print(f"{i}. {c.name}")

choice = int(input('Your choice: '))
selected_char = characters[choice - 1]

interface(selected_char)

print('final stats:')
selected_char.display_stats()



