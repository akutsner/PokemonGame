#Imports

#done

import requests
from requests import JSONDecodeError

#librarys

from flask import Flask, request

#Classes
from Classes.PokemonClass import PokemonStats

app = Flask(__name__)
pokemon_team = []
pokemon_enemy_team = []
@app.route("/")
def home():
    """
    :inputs: User input
    :return: HTML strings or pokemon objects and images, buttons and text boxes
    """
    title = """
            <h1> Pokemon </h1><br>
        """
    pokemon = """
            <h3> Pokemon Team </h3><br>
        """
    pokemon_display_str = "<div style='display: flex; flex-wrap: wrap;'>"

    if len(pokemon_team) < 1:
        pokemon_display_str += "Empty Team <br><br>"
    else:
        for i in range(len(pokemon_team)):
            name = pokemon_team[i].pokemon
            poke_url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
            poke_response = requests.get(poke_url)
            poke_data = poke_response.json()
            sprite = poke_data["sprites"]["front_default"]

            if sprite:
                pokemon_display_str += f"""
                    <div style="flex: 0 0 150px; text-align: center; margin: 10px;">
                        <img src="{sprite}" alt="{name} sprite" style="width:100px;"><br>
                        {i + 1}: {name.capitalize()}
                    </div>
                """
            else:
                pokemon_display_str += f"<div>(No image)</div>"

    pokemon_display_str += "</div>"

    pokemon_enemy_display_str = "<div style='display: flex; flex-wrap: wrap;'>"

    if len(pokemon_enemy_team) < 1:
        pokemon_enemy_display_str += "Empty Team <br>"
    else:
        for i in range(len(pokemon_enemy_team)):
            name = pokemon_enemy_team[i].pokemon
            poke_url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
            poke_response = requests.get(poke_url)
            poke_data = poke_response.json()
            sprite = poke_data["sprites"]["front_default"]

            if sprite:
                pokemon_enemy_display_str += f"""
                        <div style="flex: 0 0 150px; text-align: center; margin: 10px;">
                            <img src="{sprite}" alt="{name} sprite" style="width:100px;"><br>
                            {i + 1}: {name.capitalize()}
                        </div>
                    """
            else:
                pokemon_enemy_display_str += f"<div> (No image)</div>"

    pokemon_enemy_display_str += "</div>"

#------------------------------------------------------------------------------------------------------------------------

    add_pokemon_form = """
            <form action="/addpok" method="POST">
                <input type='text' name='new_pok' placeholder="Enter Pokémon name">
                <input type='submit' value='Add Pokemon to home team'>
            </form>
        """

    add_enemy_pokemon_form = """
            <br><form action="/addenemypok" method="POST">
                 <input type='text' name='new_pok' placeholder="Enter Pokémon name">
                 <input type='submit' value='Add Pokemon to enemy team'>
            </form>
            """
    remove_pokemon_form = """
            <form action="/removepok" method="POST">
                <input type='text' name='removed_pok' placeholder="Enter Pokémon number">
                <input type='submit' value='Remove Pokemon Number'>
            </form>  
        """

    remove_enemy_form = """
                <form action="/removeenemypok" method="POST">
                    <input type='text' name='removed_pok' placeholder="Enter Pokémon number">
                    <input type='submit' value='Remove Pokemon Number'>
                </form>  
            """
    clear_all_pokemon_form = """
            <form action="/removeall" method="POST">
                <input type='submit' value='Remove Pokemon'>
            </form><br><br>  
        """

    clear_all_enemy_form = """
                <form action="/removeallenemy" method="POST">
                    <input type='submit' value='Remove Pokemon'>
                </form><br><br>  
            """

    pokemon_stats = """
            <h1>  Stats <h1>
            <form action="/stats" >
                 <input type='submit' value='Get Pokemon stats' placeholder='Enter Pokemon'>
            </form>
        """

    pokemon_bye_type = """
        <form action="/getbytype" method="post">
            <select name="get_pokemon_type">
                <option value="normal">Normal</option>
                <option value="fighting">Fighting</option>
                <option value="flying">Flying</option>
                <option value="poison">Poison</option>
                <option value="ground">Ground</option>
                <option value="rock">Rock</option>
                <option value="bug">Bug</option>
                <option value="ghost">Ghost</option>
                <option value="steel">Steel</option>
                <option value="fire">Fire</option>
                <option value="water">Water</option>
                <option value="grass">Grass</option>
                <option value="electric">Electric</option>
                <option value="psychic">Psychic</option>
                <option value="ice">Ice</option>
                <option value="dragon">Dragon</option>
                <option value="dark">Dark</option>
                <option value="fairy">Fairy</option>
            </select>
            <input type="submit" value="Get pokemon by type">
        </form>
    """



    message = title + pokemon + pokemon_display_str + add_pokemon_form + remove_pokemon_form + clear_all_pokemon_form + pokemon_enemy_display_str + add_enemy_pokemon_form + remove_enemy_form + clear_all_enemy_form + pokemon_stats + f"{pokemon_bye_type}"
    return message



#---------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/addpok", methods=["POST"])
def new_pokemon_confirmation():
    """
    Adds a new Pokémon to the team.

    :inputs: User input from a form (Pokémon name)
    :return: HTML string with a message and a link back to home
    """
    new_pok = request.form.get("new_pok", "")
    if new_pok != "" and len(pokemon_team) < 3:
        try:
            pok = PokemonStats(new_pok)
            pokemon_team.append(pok)
            message = f"{new_pok.capitalize()} added to your team!"
        except Exception:
            message = f"Could not find Pokémon '{new_pok}'. Check spelling."
    else:
        message = "No Pokémon entered or Too many Pokemon (Teams of 3)"
    return message + "<br><br><a href='/'> Back to home </a>"

@app.route("/addenemypok", methods=["POST"])
def new_enemy_confirmation():
    """
    Adds a new Pokémon to the team.

    :inputs: User input from a form (Pokémon name)
    :return: HTML string with a message and a link back to home
        """
    new_pok = request.form.get("new_pok", "")
    if new_pok != "" and len(pokemon_enemy_team) < 3:
        try:
            pok = PokemonStats(new_pok)
            pokemon_enemy_team.append(pok)
            message = f"{new_pok.capitalize()} added to your team!"
        except Exception:
            message = f"Could not find Pokémon '{new_pok}'. Check spelling."
    else:
        message = "No Pokémon entered or Too many Pokemon (Teams of 3)"
    return message + "<br><br><a href='/'> Back to home </a>"


#---------------------------------------------------------------------------------------------------------------------------------------------------



@app.route("/removepok", methods=["POST"])
def remove_pokemon_confirmation():
    """
    Removes a Pokémon from the team based on user input.

    :inputs: User input from a form (index of Pokémon to remove)
    :return: HTML string with a message and a link back to home
       """
    removed_note = request.form.get("removed_pok", "")
    try:
        removed_index = int(removed_note) - 1
        if 0 <= removed_index < len(pokemon_team):
            removed_pokemon = pokemon_team[removed_index].pokemon.capitalize()
            for i in range(removed_index, len(pokemon_team) - 1):
                pokemon_team[i] = pokemon_team[i + 1]
            pokemon_team[0:len(pokemon_team)] = pokemon_team[0:len(pokemon_team) - 1]
            message = f"Removed {removed_pokemon} from team."
        else:
            message = "Invalid index."
    except ValueError:
        message = "Invalid input."

    return message + "<br><br><a href='/'> Back to home </a>"

@app.route("/removeenemypok", methods=["POST"])
def remove_enemy_confirmation():
    """
    Removes a Pokémon from the team based on user input.

    :inputs: User input from a form (index of Pokémon to remove)
    :return: HTML string with a message and a link back to home
       """
    removed_note = request.form.get("removed_pok", "")
    try:
        removed_index = int(removed_note) - 1
        if 0 <= removed_index < len(pokemon_enemy_team):
            removed_pokemon = pokemon_enemy_team[removed_index].pokemon.capitalize()
            for i in range(removed_index, len(pokemon_enemy_team) - 1):
                pokemon_enemy_team[i] = pokemon_enemy_team[i + 1]
            pokemon_enemy_team[0:len(pokemon_enemy_team)] = pokemon_enemy_team[0:len(pokemon_enemy_team) - 1]
            message = f"Removed {removed_pokemon} from team."
        else:
            message = "Invalid index."
    except ValueError:
        message = "Invalid input."

    return message + "<br><br><a href='/'> Back to home </a>"

#---------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/removeall", methods=["POST"])
def remove_all_confimation():
    """
    Removes all Pokémon from the team.

    :inputs: None (button press triggers POST)
    :return: HTML string with a message and a link back to home
        """
    pokemon_team[0:len(pokemon_team)] = []
    message = "Pokemon Removed."
    return message + "<br><br><a href='/'>Back to home</a>"

@app.route("/removeallenemy", methods=["POST"])
def remove_all__enemy_confimation():
    """
    Removes all Pokémon from the team.

    :inputs: None (button press triggers POST)
    :return: HTML string with a message and a link back to home
    """
    pokemon_enemy_team[0:len(pokemon_enemy_team)] = []
    message = "Pokemon Removed."
    return message + "<br><br><a href='/'>Back to home</a>"



#---------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/stats")
def stats():
    """
    Displays the Pokémon team and forms to view stats, types, and evolutions.

    :inputs: None directly (user can enter data on this page)
    :return: HTML string with team info, inputs, and a link back to home
        """
    title = """
            <h1> Pokemon Stats </h1>
            """
    pokemon_display_str = "<br> Home Team<br>"
    for i in range(len(pokemon_team)):
        pokemon_display_str += f"{i + 1}: {pokemon_team[i]}<br>" + f"<br>"

    pokemon_enemy_display_str = "<br> Enemy Team<br>"
    for i in range(len(pokemon_enemy_team)):
        pokemon_enemy_display_str += f"{i + 1}: {pokemon_enemy_team[i]}<br>" + f"<br>"

    pokemon_stat_form = """
            <form action="/getstat" method="post">
                <input type="text" name="get_pokemon" placeholder="Enter Pokémon name"><br><br>
                <select name="stat">
                    <option value="hp">HP</option>
                    <option value="defense">Defense</option>
                    <option value="special_defense">Special Defense</option>
                    <option value="attack">Attack</option>
                    <option value="special_attack">Special Attack</option>
                    <option value="speed">Speed</option>
                    <option value="weaknesses">Weaknesses</option>
                </select>
                <input type="submit" value="Get Stat">
            </form><br><br>
            """
    get_all_stats = """<form action="/get_all_stats" method="POST">
                            <input type='text' name="get_pokemon_stats" placeholder="Enter Pokémon name">
                            <input type='submit' value='Get Pokemon stats' >
                        </form><br><br>
                        """
    get_type = """<form action="/gettype" method="POST">
                            <input type='text' name="get_pokemon" placeholder="Enter Pokémon name">
                            <input type='submit' value='Get Pokemon Types' >
                        </form><br><br>
                        """
    get_evo = """<form action="/getevo" method="POST">
                            <input type='text' name="get_pokemon" placeholder="Enter Pokémon name">
                            <input type='submit' value='Get Pokemon Evolution Chain' >
                        </form><br><br>
                                """



    return title + pokemon_display_str + pokemon_enemy_display_str + pokemon_stat_form + get_type + get_all_stats + get_evo+"<br><br><a href='/'> Back to Home </a>"


#---------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/getstat",  methods=["POST"])
def get_stats_comfirmation():
    """
    Returns the selected stat for a given Pokémon.

    :inputs: Pokémon name and stat type from form
    :return: HTML string showing the stat value or error message, plus link back to stats page
        """
    pokemon = request.form.get("get_pokemon", "")
    stat = request.form.get("stat", "")
    if pokemon != "":
        try:
            pok = PokemonStats(pokemon)
            if stat == "hp":
                message = f"{pok.pokemon.capitalize()}'s Health Points is {pok.hp}."
            elif stat == "defense":
                message = f"{pok.pokemon.capitalize()}'s Defense is {pok.defense}."
            elif stat == "special_defense":
                message = f"{pok.pokemon.capitalize()}'s Special Defense is {pok.special_defense}."
            elif stat == "attack":
                message = f"{pok.pokemon.capitalize()}'s Attack is {pok.attack} damage."
            elif stat == "special_attack":
                message = f"{pok.pokemon.capitalize()}'s Special Attack is {pok.special_attack} damage."
            elif stat == "speed":
                message = f"{pok.pokemon.capitalize()}'s Speed is {pok.speed}."
            elif stat == "weaknesses":
                message = f"{pok.pokemon.capitalize()}'s Weaknesses are: {pok.weaknesses}."
            else:
                message = "Invalid stat requested."
        except JSONDecodeError:
            message = f"Data for '{pokemon}' not found."
    else:
        message = f"Data for '{pokemon}' not found."
    return message + "<br><br><a href='/stats'>Back to Stats</a>"


#---------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/getbytype", methods=["POST"])
def get_by_type_confirmation():
    """
    Shows a list of Pokémon that match a given type, with images.

    :inputs: User input (Pokémon type)
    :return: HTML string with Pokémon images and names or an error message
        """
    pokemon_type = request.form.get("get_pokemon_type", "").lower()

    if pokemon_type:
        url = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
        try:
            response = requests.get(url).json()
            pokemon_list = response.get("pokemon", [])
            if not pokemon_list:
                message = f"No Pokémon found for type '{pokemon_type}'."
            else:
                message = "<h2>List of Pokémon:</h2><div style='display:flex; flex-wrap:wrap;'>"

                for entry in pokemon_list:
                    name = entry["pokemon"]["name"]
                    poke_url = entry["pokemon"]["url"]

                    poke_response = requests.get(poke_url)
                    poke_data = poke_response.json()
                    sprite = poke_data["sprites"]["front_default"]

                    if sprite:
                        message += f"""
                            <div style="flex: 0 0 150px; text-align: center; margin: 10px;">
                                <img src="{sprite}" alt="{name} sprite" style="width:100px;"><br>
                                {name.capitalize()}
                            </div>
                            """

                message += "</div>"

        except requests.RequestException:
            message = f"Failed to retrieve data for type '{pokemon_type}'."
    else:
        message = "Please provide a Pokémon type."

    return f"""
        <h1>Pokémon for type: {pokemon_type}</h1>
        <h6>{message}</h6>
        <br><br><a href='/'>Back to Home</a>
    """



#---------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/getevo", methods=["POST"])
def evo_confirmation():
    """
    Displays the evolution chain for a given Pokémon.

    :inputs: User input from form (Pokémon name)
    :return: HTML string with the evolution list or an error message
        """
    pokemon = request.form.get("get_pokemon", "")
    if pokemon != "":
        try:
            species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.lower()}"
            response = requests.get(species_url)
            species_data = response.json()

            evo_chain_url = species_data['evolution_chain']['url']
            evo_response = requests.get(evo_chain_url)
            evo_data = evo_response.json()

            chain = evo_data['chain']
            evo_list = []

            while chain:
                evo_list.append(chain['species']['name'])
                if chain['evolves_to']:
                    chain = chain['evolves_to'][0]
                else:
                    chain = None

            message = f" {evo_list}"

        except requests.exceptions.RequestException:
            message = f"Type '{pokemon}' not found."""
    else:
        message = "Invalid"
    return message + "<br><br><a href='/stats'> Back to Home </a>"

#---------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/gettype", methods=["POST"])
def type_confirmation():
    """
    Shows the type of a given Pokémon.

    :inputs: User input from form (Pokémon name)
    :return: HTML string with the Pokémon type or an error message
        """
    pokemon = request.form.get("get_pokemon", "")
    if pokemon != "":
        try:
            pok = PokemonStats(pokemon)
            message = f"Type of {pokemon} is {pok.type}."
        except JSONDecodeError:
            message = (f"Type for '{pokemon}' not found.")
    else:
        message = "Invalid"
    return message + "<br><br><a href='/stats'> Back to Home </a>"

#---------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/get_all_stats", methods=["POST"])
def stats_confirmation():
    """
    Displays detailed stats for a given Pokémon.

    :inputs: User input from form (Pokémon name)
    :return: HTML string with detailed Pokémon stats or an error message
        """
    pokemon = request.form.get("get_pokemon_stats", "")
    if pokemon != "":
        try:
            pok = PokemonStats(pokemon)
            big_str = f"Pokemon: {pok.pokemon.capitalize()}<br>" f"Pokemon type: {pok.type}<br>" f"HP: {pok.hp}<br>" f"Defense: {pok.defense}<br>" f"Special Defense: {pok.special_defense}<br>" f"Attack: {pok.attack}<br>" f"Special Attack: {pok.special_attack}<br>" f"Speed: {pok.speed}<br>" f"Weaknesses: {pok.weaknesses}."
            message = big_str
        except JSONDecodeError:
            message = f"The Pokemon {pokemon} not found. Check spelling!"
    else:
        message = "Invalid"
    return message + "<br><br><a href='/stats'> Back to Home </a>"

#--------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)