import unittest
import json

from Classes.PokemonClass import PokemonStats
import CLI.PokemonCLI

class TestPokemonStats(unittest.TestCase):

    def test_hp(self):
        with open("pokemon_test.json", "r") as file:
            mock_response = json.load(file)
        pokemon = PokemonStats("gengar")
        response = pokemon.get_stat("gengar", "hp")
        self.assertEqual(response, mock_response["stats"][0]["base_stat"])

        response = pokemon.get_stat("genga","hp")
        self.assertEqual(response, "Hp data for 'genga' not found.")

    def test_attack(self):
        with open("pokemon_test.json", "r") as file:
            mock_response = json.load(file)
        pokemon = PokemonStats("gengar")
        response = pokemon.get_stat("gengar", "attack")
        self.assertEqual(response, mock_response["stats"][1]["base_stat"])

        response = pokemon.get_stat("genga", "attack")
        self.assertEqual(response, "Attack data for 'genga' not found.")

    def test_defense(self):
        with open("pokemon_test.json", "r") as file:
            mock_response = json.load(file)
        pokemon = PokemonStats("gengar")
        response = pokemon.get_stat("gengar", "defense")
        self.assertEqual(response, mock_response["stats"][2]["base_stat"])

        response = pokemon.get_stat("genga", "defense")
        self.assertEqual(response, "Defense data for 'genga' not found.")

    def test_special_defense(self):
        with open("pokemon_test.json", "r") as file:
            mock_response = json.load(file)
        pokemon = PokemonStats("gengar")
        response = pokemon.get_stat("gengar", "special-defense")
        self.assertEqual(response, mock_response["stats"][4]["base_stat"])

        response = pokemon.get_stat("genga", "special-defense")
        self.assertEqual(response, "Special-defense data for 'genga' not found.")

    def test_special_attack(self):
        with open("pokemon_test.json", "r") as file:
            json_response = json.load(file)
        pokemon = PokemonStats("gengar")
        response = pokemon.get_stat("gengar", "special-attack")
        self.assertEqual(response, json_response["stats"][3]["base_stat"])

        response = pokemon.get_stat("genga", "special-attack")
        self.assertEqual(response, "Special-attack data for 'genga' not found.")

    def test_speed(self):
        with open("pokemon_test.json", "r") as file:
            json_response = json.load(file)
        pokemon = PokemonStats("gengar")
        response = pokemon.get_stat("gengar", "speed")
        self.assertEqual(response, json_response["stats"][5]["base_stat"])

        response = pokemon.get_stat("genga", "speed")
        self.assertEqual(response, "Speed data for 'genga' not found.")

    def test_weaknesses(self):
        pokemon = PokemonStats("gengar")
        response = pokemon.get_weaknesses("gengar")
        self.assertEqual(response, ['ghost', 'dark', 'ground', 'psychic'])

    def test_get_type(self):
        with open("pokemon_test.json", "r") as file:
            json_response = json.load(file)
        pokemon = PokemonStats("gengar")
        response = pokemon.get_type("gengar")
        list = [json_response["types"][0]["type"]["name"], json_response["types"][1]["type"]["name"]]
        self.assertEqual(response, list)

    def test_get_pokemon_by_type(self):
        pokemon = CLI.PokemonCLI.get_pokemon_by_type("fire")
        self.assertIn("charizard", pokemon)

if __name__ == '__main__':
    unittest.main()
