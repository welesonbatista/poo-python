class Character:
    def __init__(self, name, health, level):
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_level(self):
        return self.__level

    def get_details(self):
        return f"Name: {self.get_name()},\nHealth: {self.get_health()}\nLevel: {self.get_level()}"

    def attack(self, target):
        damage = self.get_level() * 2
        target.take_damage(damage)
        print(f"{self.get_name()} attacked {target.get_name()} and dealt {damage} damage")
    
    def take_damage (self, damage):
        self.__health -= damage
        if self.__health <= 0:
            self.__health = 0


class Hero(Character):
    def __init__(self, name, health, level, skill):
        super().__init__(name, health, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def get_details(self):
        return f"{super().get_details()}\nSkill: {self.get_skill()}\n"

    def special_attack(self, target):
        damage = self.get_level()* 5
        target.take_damage(damage)
        print(f"{self.get_name()} used the special skill {self.get_skill()} on {target.get_name()} and took {damage} damage")

        


class Enemy(Character):
    def __init__(self, name, health, level, enemy_type):
        super().__init__(name, health, level)
        self.__enemy_type = enemy_type

    def get_type(self):
        return self.__enemy_type

    def get_details(self):
        return f"{super().get_details()}\nEnemy Type: {self.get_type()}\n"


class Game:
    """Game management class"""

    def __init__(self):
        self.hero = Hero(name="Hero", health=100, level=30, skill="Super Power")
        self.enemy = Enemy(name="Enemy", health=300, level=20, enemy_type="Flying")

    def battle_start(self):
        print("Starting battle, take care and good luck!!")

        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("\nCharacter details:")
            print(self.hero.get_details())
            print(self.enemy.get_details())

            input("Press Enter to attack...")
            choice = input("Choice (1 - Normal attack, 2 - Special attack): ")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
              self.hero.special_attack(self.enemy)
            else:
                print("Invalid choice, try again")
            
            if self.enemy.get_health()>0:
                self.enemy.attack(self.hero)
          
        if self.hero.get_health() > 0:
          print("\n congratulations, you win the battle!")
        else:
          print("\n You lose HAHAHAH!")


game = Game()
game.battle_start()