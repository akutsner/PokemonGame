import unittest
from Classes import FightClass
from Classes.PokemonClass import PokemonStats

class TestFightPok(unittest.TestCase):
    def test_normal_attack(self):
        pokemon1 = PokemonStats("Gengar")
        pokemon2 = PokemonStats("Charizard")
        fight = FightClass.Fight_pok(pokemon1.pokemon, pokemon2.pokemon)
        fight.pokemon1 = pokemon1
        fight.pokemon2 = pokemon2
        fight.current_turn = pokemon1
        fight.opponent = pokemon2

        initial_hp = pokemon2.hp
        fight.fight("1")

        expected_damage = (pokemon1.attack - pokemon2.defense // 2) // 2
        self.assertEqual(pokemon2.hp, initial_hp - expected_damage)

    def test_special_attack(self):
        pokemon1 = PokemonStats("gengar")
        pokemon2 = PokemonStats("Charizard")

        fight = FightClass.Fight_pok(pokemon1.pokemon, pokemon2.pokemon)
        fight.pokemon1 = pokemon1
        fight.pokemon2 = pokemon2
        fight.current_turn = pokemon1
        fight.opponent = pokemon2

        initial_hp = pokemon2.hp
        fight.fight("2")

        expected_damage = (pokemon1.special_attack - pokemon2.defense // 3) // 2
        self.assertEqual(pokemon2.hp, initial_hp - expected_damage)
        self.assertTrue(fight.pokemon1_special_used)

    def test_special_defense(self):
        pokemon1 = PokemonStats("gengar")
        pokemon2 = PokemonStats("charizard")
        fight = FightClass.Fight_pok(pokemon1.pokemon, pokemon2.pokemon)
        fight.pokemon2 = pokemon2


        fight.fight("3")


        self.assertEqual(pokemon2.hp, 78)


    def test_turn_switching(self):
        pokemon1 = PokemonStats("gengar")
        pokemon2 = PokemonStats("charizard")

        fight = FightClass.Fight_pok(pokemon1.pokemon, pokemon2.pokemon)
        fight.pokemon1 = pokemon1
        fight.pokemon2 = pokemon2
        fight.current_turn = pokemon1
        fight.opponent = pokemon2

        fight.fight("1")
        self.assertEqual(fight.current_turn, pokemon2)
        self.assertEqual(fight.opponent, pokemon1)


if __name__ == "__main__":
    unittest.main()
