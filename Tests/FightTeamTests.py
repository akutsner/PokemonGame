import unittest

from Classes.PokemonTeamClass import PokemonTeam


class PokemonTeamTests(unittest.TestCase):


    def test_add_and_get_next_pokemon(self):
        team = PokemonTeam("Ash")
        team.add_pokemon("Pikachu")
        poke1 = team.get_next_pokemon()
        self.assertEqual(poke1.pokemon, "pikachu")


        team.add_pokemon("Bulbasaur")
        poke2 = team.get_next_pokemon()
        self.assertEqual(poke2.pokemon, "bulbasaur")


        poke3 = team.get_next_pokemon()
        self.assertEqual(poke3, None)

    def test_has_usable_pokemon(self):
        team = PokemonTeam("Gary")
        self.assertFalse(team.has_usable_pokemon())  # Empty team

        team.add_pokemon("Squirtle")
        self.assertTrue(team.has_usable_pokemon())

