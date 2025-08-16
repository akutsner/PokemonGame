#done
import requests
import json

from requests import JSONDecodeError


class PokemonStats:
    def __init__(self, pokemon_name):
        self.pokemon = pokemon_name.lower()
        self.hp = self.get_stat(self.pokemon, "hp")
        self.defense = self.get_stat(self.pokemon, "defense")
        self.special_defense = self.get_stat(self.pokemon, "special-defense")
        self.attack = self.get_stat(self.pokemon, "attack")
        self.special_attack = self.get_stat(self.pokemon, "special-attack")
        self.speed = self.get_stat(self.pokemon, "speed")
        self.weaknesses = self.get_weaknesses(self.pokemon)
        self.type = self.get_type(self.pokemon)

    def __str__(self):
        return (f"Pokemon: {self.pokemon.capitalize()}\n" f"Pokemon type: {self.type}\n" f"HP: {self.hp}\n" f"Defense: {self.defense}\n" f"Special Defense: {self.special_defense}\n" f"Attack: {self.attack}\n" f"Special Attack: {self.special_attack}\n" f"Speed: {self.speed}\n" f"Weaknesses: {self.weaknesses}.")

    def get_url(self, pokemon_name):
        """
        Returns URL
        :param pokemon_name: Name of the pokemon
        :return: URL
        """
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        return requests.get(url)

    def get_stat(self, pokemon_name, stat_name):
        """
        Takes in stat type and Pokemon name and returns the given stat from the API
        :param pokemon_name: Pokemon Name
        :param stat_name: the entered stat name
        :return: stats
        """
        try:
            data = self.get_url(pokemon_name).json()
            for stat in data["stats"]:
                if stat["stat"]["name"] == stat_name:
                    return stat["base_stat"]
        except  JSONDecodeError:
            return f"{stat_name.capitalize()} data for '{pokemon_name}' not found."


    def get_weaknesses(self, pokemon_name):
        '''
        Takes a CSV file and turns it into a json file. Loops through the file until it finds whats needed. Opens the next url.
        :return: returns a list of weaknesses of the pokemon
        '''
        data = self.get_url(pokemon_name).json()
        if not data:  # This returns an empty list if the pokemon doesn't have a weakness
            return []
        try:
            weaknesses = []
            for type_info in data['types']:
                type_url = type_info['type']['url']
                type_data = requests.get(type_url).json()
                for damage_relation in type_data['damage_relations']['double_damage_from']:
                    weaknesses.append(damage_relation['name'])
            return weaknesses
        except JSONDecodeError:
            return []

    def get_type(self, pokemon_name):
        '''
        Takes a CSV file and turns it into a json file. Loops through the file until it finds the pokemons type.
        :param pokemon_name: Name of pokemon
        :return: List of pokemon's types
        '''
        data = self.get_url(pokemon_name).json()
        try:
            types = []
            for type_info in data['types']:
                type_name = type_info['type']['name']
                types.append(type_name)
            return types

        except JSONDecodeError:
            return f"Type not found for {pokemon_name}"
