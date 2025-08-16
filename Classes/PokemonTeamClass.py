#done
from Classes.PokemonClass import PokemonStats



class PokemonTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.team = []
        self.current_index = 0

    def add_pokemon(self, pokemon_name):
        """Add a Pokémon to the team."""
        self.team.append(pokemon_name)

    def get_next_pokemon(self):
        """Return the next available Pokémon from the team."""
        while self.current_index < len(self.team):
            pokemon = PokemonStats(self.team[self.current_index])
            if pokemon.hp > 0:
                self.current_index += 1
                return pokemon
            else:
                self.current_index += 1
        return None


    def has_usable_pokemon(self):
        """
        Check if any Pokémon in the team has HP left.
        :returns: True or False
        """
        for name in self.team:
            pokemon = PokemonStats(name)
            if pokemon.hp > 0:
                return True
        return False

    def reset_team(self):
        """Reset index to reuse the team (e.g., for a new battle)."""
        self.current_index = 0
