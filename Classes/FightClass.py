#done
from Classes.PokemonClass import PokemonStats

class Fight_pok:
    def __init__(self, pokemon1, pokemon2):

        self.pokemon1 = PokemonStats(pokemon1)
        self.pokemon1_name = pokemon1
        self.pokemon2 = PokemonStats(pokemon2)
        self.pokemon2_name = pokemon2

        if self.pokemon1.speed >= self.pokemon2.speed:
            self.current_turn = self.pokemon1
        else:
            self.current_turn = self.pokemon2

        if self.current_turn == self.pokemon1:
            self.opponent = self.pokemon2
        else:
            self.opponent = self.pokemon1

        self.pokemon1_special_used = False
        self.pokemon2_special_used = False
        self.pokemon1_special_defense_used = False
        self.pokemon2_special_defense_used = False

        self.winsp1 = 0
        self.winsp2 = 0

    def start_battle(self):
        """
        Starts a battle between two Pokémon, alternating turns until one is defeated.

        :inputs: None
        :return: A message indicating the winner of the battle
           """
        while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
            choice = input(f"{self.current_turn.pokemon}'s turn. Choose move:\n1. Normal Attack\n2. Special Attack\n3. Special Defense\nChoice: ")
            self.fight(choice)

        if self.pokemon1.hp > 0:
            winner = self.pokemon1
            self.winsp1 += 1
        else:
            winner = self.pokemon2
            self.winsp2 += 1
        message  = f"{winner.pokemon} wins the battle!\n"

        return message

    def fight(self, choice):
        """
        Executes a battle move based on the player's choice and alternates turns.

        :inputs: choice (str)
        :return: None (prints the result of the move or an error message)
            """
        if choice == "1":
            move_type = "Normal"
            print(self.attack(self.current_turn, self.opponent, move_type))
        elif choice == "2" and not self.special_used(self.current_turn):
            move_type = "Special"
            print(self.attack(self.current_turn, self.opponent, move_type))
            self.use_special(self.current_turn)
        elif choice == "3" and not self.special_defense_used(self.current_turn):
            print(self.apply_special_defense(self.current_turn))
            self.use_special_defense(self.current_turn)
        else:
            print(f"\nInvalid Input! OH NO! You lost a turn. Its now {self.opponent.pokemon}'s turn")

        swap = self.current_turn
        self.current_turn = self.opponent
        self.opponent = swap

    def special_used(self, pokemon):
        """
        Checks if a Pokémon has already used its special attack.

        :param: pokemon: name
        :return: True if the Pokémon has used
            """
        if pokemon == self.pokemon1:
            return self.pokemon1_special_used
        else:
            return self.pokemon2_special_used

    def use_special(self, pokemon):
        """
        Marks a Pokémon as having used its special attack.

        :param: pokemon name
        :return: None (changes the attributes value)
            """
        if pokemon == self.pokemon1:
            self.pokemon1_special_used = True
        else:
            self.pokemon2_special_used = True

    def special_defense_used(self, pokemon):
        """
        Checks if a Pokémon has already used its special defense.

        :param: pokemon: name
        :return: True if the Pokémon has used
        """
        if pokemon == self.pokemon1:
            return self.pokemon1_special_defense_used
        else:
            return self.pokemon2_special_defense_used

    def use_special_defense(self, pokemon):
        """
        Marks a Pokémon as having used its special defense.

        :param: pokemon name
        :return: None (changes the attributes value)
            """
        if pokemon == self.pokemon1:
            self.pokemon1_special_defense_used = True
        else:
            self.pokemon2_special_defense_used = True

    def apply_special_defense(self, defender):
        """
        Applies HP to the pokemons total health
        :param defender: Pokemon using defense
        :return: Str
        """
        if defender == self.pokemon1:
            points = defender.special_defense // 2
            self.pokemon1.hp += points
            return f"\n{defender.pokemon} used Special Defense! Increased HP by {points}. {defender.pokemon}'s HP is now {defender.hp}."
        else:
            points = defender.special_defense // 2
            self.pokemon2.hp += points
            return f"\n{defender.pokemon} used Special Defense! Increased HP by {points}. {defender.pokemon}'s HP is now {defender.hp}."

    def attack(self, attacker, defender, move_type):
        """
        Applies the damage from an attack
        :param attacker: Current turn pokemon object
        :param defender: Other Pokemon taking the damage
        :param move_type: Special or normal
        :return: str
        """
        if move_type == "Special":
            damage = attacker.special_attack - defender.defense // 3
        else:
            damage = attacker.attack - defender.defense // 2

        buffered_damage = damage // 2
        defender.hp -= buffered_damage
        if defender.hp < 0:
            defender.hp = 0
        return f"\n{attacker.pokemon} used {move_type} Attack! Dealt {buffered_damage} damage. {defender.pokemon} has {defender.hp} HP left."

