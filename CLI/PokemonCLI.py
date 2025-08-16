import os
import random
import time


import requests
from requests import JSONDecodeError

from Classes.PokemonClass import PokemonStats
from Classes.FightClass import Fight_pok

from PIL import Image, ImageOps


def pokemon_cli():
    continue1 = True
    while continue1 == True:
        print("\nPokémon Info")
        print("1. Get Pokémon by Type")
        print("2. Get Pokémon Evolution Line")
        print("3. To Open individual stats menu")
        print("4. Get all stats")
        print("5. Get Picture of Pokemon")
        print("6. Play Who's that pokemon")
        print("7. Get Item Picture (Pokeballs and Potions)")
        print("M. To play a match!")
        print("Q. Exit")
        choice = input("\nEnter choice: ")

        if choice == '1':
            print(
                "\nNormal, Fighting, Flying, Poison,\nGround, Rock, Bug, Ghost,\nSteel, Fire, Water, Grass,\nElectric, psychic, Ice, Dragon,\nDark, Fairy\n")
            ptype = input("Enter Pokémon type: ", )
            print(get_pokemon_by_type(ptype))
            type_image = get_type_image(ptype)
            show_type_image(type_image)
        elif choice == '2':
            pname = input("Enter Pokémon name: ", )
            print(get_pokemon_evolution_chain(pname))
        elif choice == '4':
            pname = input("Enter Pokémon name: ", )
            print(get_all_stats(pname))
        elif choice == '5':
            pname = input("Enter Pokémon name: ", )
            type = input("Enter 's' to get shiny version or anything for regular: ", )
            image_url = get_picture(pname, type)
            show_image(image_url)
        elif choice == '6':
            play_who_is_that_pokemon()
        elif choice == '7':
            inum = input("Enter Item number: ", )
            image_url = get_item_picture(inum)
            show_image(image_url)
            get_item_name(inum)
        elif choice == 'M' or choice == "m":
            play_match()
        elif choice == 'Q' or choice == 'q':
            continue1 = False
            print("Goodbye!")
        elif choice == "3":
            print("1. Get Pokémon HP")
            print("2. Get Pokémon Defense")
            print("3. Get Pokémon Special Defense Move")
            print("4. Get Pokémon Normal Attack")
            print("5. Get Pokémon Special Attack")
            print("6. Get Pokémon Speed")
            print("7. Get Pokémon Weaknesses")
            print("8. Get Pokémon Type")
            choice2 = input("\nEnter choice: ")
            if choice2 == '1':
                pname = input("Enter Pokémon name: ", )
                print(get_hp(pname))
            elif choice2 == '2':
                pname = input("Enter Pokémon name: ", )
                print(get_defense(pname))
            elif choice2 == '3':
                pname = input("Enter Pokémon name: ", )
                print(get_sd(pname))
            elif choice2 == '4':
                pname = input("Enter Pokémon name: ", )
                print(get_na(pname))
            elif choice2 == '5':
                pname = input("Enter Pokémon name: ", )
                print(get_sa(pname))
            elif choice2 == '6':
                pname = input("Enter Pokémon name: ", )
                print(get_speed(pname))
            elif choice2 == '7':
                pname = input("Enter Pokémon name: ", )
                print(get_weakness(pname))
            elif choice2 == '8':
                pname = input("Enter Pokémon name: ", )
                print(get_type(pname))
            else:
                print("Invalid choice. Try again.")
        else:
            print("Invalid choice. Try again.")

def get_pokemon_by_type(pokemon_type):
    '''
    Gives a list of Pokemon of the entered type
    :param pokemon_type: Takes user input of the type of Pokemon. Should return "not found" if type entered is not in the API
    :return: List of Str of Pokemon Names
        '''
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"

    try:
        data = requests.get(url).json()
        if 'pokemon' in data:
            data = requests.get(url).json()
            pokemon_names = []
            for pokemon in data['pokemon']:
                pokemon_names.append(pokemon['pokemon']['name'])
            return pokemon_names

    except JSONDecodeError:
        return f"Type '{pokemon_type}' not found."

def get_type_image(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"

    response = requests.get(url)
    data = response.json()
    sprite_url = data["sprites"]["generation-iii"]["colosseum"]["name_icon"]
    return sprite_url

def show_type_image(image_url):
    image_data = requests.get(image_url).content
    image_path = "pokemon_image.jpg"
    with open(image_path, 'wb') as file:
        file.write(image_data)

    im = Image.open(image_path)
    out = im.resize((700, 200))
    out.show()
    os.remove(image_path)

def get_pokemon_evolution_chain(pokemon_name):
    '''
    Enters Pokemon Name and will get the rest of the stages
    :param pokemon_name: Takes user input of the type of Pokemon. Should return "not found" if type entered is not in the API
    :return: List of the names of each evolution in the chain. Can enter any part of the chain and will get the rest.
        '''
    try:
        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
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

        return evo_list

    except requests.exceptions.RequestException:
        return f"Type '{pokemon_name}' not found."

def get_hp(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Pokemon's Health Points are {pok.hp}."
    except JSONDecodeError:
        return f"HP data for '{pokemon}' not found."

def get_defense(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Pokemon Defense is {pok.defense}."
    except JSONDecodeError:
        return f"Defense data for '{pokemon}' not found."

def get_sd(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Pokemon Special Defense is {pok.special_defense}."
    except JSONDecodeError:
        return f"Special Defense data for '{pokemon}' not found."

def get_na(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Normal Attack is {pok.attack} damage."
    except JSONDecodeError:
        return f"Normal Attack data for '{pokemon}' not found."

def get_sa(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Special Attack is {pok.special_attack} damage."
    except JSONDecodeError:
        return f"Special Attack data for '{pokemon}' not found."

def get_speed(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Speed is {pok.speed}."
    except JSONDecodeError:
        return f"Speed data for '{pokemon}' not found."

def get_weakness(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Weaknesses are: {pok.weaknesses}."
    except JSONDecodeError:
        return f"Weaknesses for '{pokemon}' not found."

def get_type(pokemon):
    try:
        pok = PokemonStats(pokemon)
        return f"Type of {pokemon} is {pok.type}."
    except JSONDecodeError:
        return (f"Type for '{pokemon}' not found.")

def get_all_stats(pokemon):
    try:
        pok = PokemonStats(pokemon)
        big_str = pok.__str__()
        return big_str
    except JSONDecodeError:
        return f"The Pokemon {pokemon} not found. Check spelling!"

#--------------------------------------------------------------------------------------------------------------------------------------------------------


    # PLAY MATCH

def play_match():
    try:
        pok1 = input("Enter First Pokémon name: ")
        pok2 = input("Enter Second Pokémon name: ")
        fight = Fight_pok(pok1, pok2)
        print(f"\n{pok1} vs {pok2}!")

        while fight.pokemon1.hp > 0 and fight.pokemon2.hp > 0:
            print(f"\n{fight.current_turn.pokemon}'s turn!")
            move_type = ""
            while move_type not in ["1", "2", "3"]:
                move_type = input("Choose attack: \n1. Normal Attack \n2. Special Attack (can only use once)\n3. Special Defense (can only use once)\n")
            fight.fight(move_type)
            print(f"\n{fight.pokemon1.pokemon} HP: {fight.pokemon1.hp}")
            print(f"{fight.pokemon2.pokemon} HP: {fight.pokemon2.hp}")

        print(fight.start_battle())
        time.sleep(4)
    except JSONDecodeError:
        return f"Check spelling!"

#--------------------------------------------------------------------------------------------------------------------------------------------------------


    # GET PICTURE FUNCTIONS

def get_picture(pokemon_name, type):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        data = response.json()
        if type == "s":
            sprite_url = data["sprites"]["front_shiny"]
        else:
            sprite_url = data["sprites"]["front_default"]
        return sprite_url
    except JSONDecodeError:
        return f"The Pokemon {pokemon_name} not found. Check spelling!"

def get_random_pokemon_pic(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    data = response.json()
    sprite_url = data["sprites"]["front_default"]
    return sprite_url

def get_item_picture(item_number):
    try:
        url = f"https://pokeapi.co/api/v2/item/{item_number.lower()}"
        response = requests.get(url)
        data = response.json()
        sprite_url = data["sprites"]["default"]
        return sprite_url
    except JSONDecodeError:
        return f"The item number {item_number} not found. Check spelling!"
#--------------------------------------------------------------------------------------------------------------------------------------------------------


    # GET NAME FUNCTIONS

def get_random_pokemon_name():
    poke_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(url)
    data = response.json()
    name = data["name"].capitalize()
    return name

def get_item_name(item_number):
    try:
        url = f"https://pokeapi.co/api/v2/item/{item_number.lower()}"
        response = requests.get(url)
        data = response.json()
        sprite_name = data["name"]
        print("This item is a",sprite_name)
    except JSONDecodeError:
        return f"The item number {item_number} not found. Check spelling!"

#--------------------------------------------------------------------------------------------------------------------------------------------------------


    # SHOWING IMAGES

def show_image(image_url):
    image_data = requests.get(image_url).content
    image_path = "pokemon_image.jpg"
    with open(image_path, 'wb') as file:
        file.write(image_data)

    im = Image.open(image_path)
    out = im.resize((700, 700))
    out.show()
    os.remove(image_path)

#--------------------------------------------------------------------------------------------------------------------------------------------------------


    # PLAY WHOS THAT POKEMON

def create_silhouette(image_url, filename):
    """Convert a Pokémon sprite into a simpler black silhouette."""
    response = requests.get(image_url)
    img_path = f"pokemon_{filename}.png"

    with open(img_path, 'wb') as image:
        image.write(response.content)

    img = Image.open(img_path).convert("RGBA")
    grayscale = ImageOps.grayscale(img)
    threshold = grayscale.copy()
    pixels = threshold.load()
    for x in range(threshold.width):
        for y in range(threshold.height):
            if pixels[x, y] < 30:
                pixels[x, y] = 0
            else:
                pixels[x, y] = 255

    silhouette = Image.new("RGBA", img.size, (0, 0, 0, 255))
    img = Image.composite(silhouette, img, threshold)

    silhouette_path = f"pokemon_silhouette_{filename}.png"
    img.save(silhouette_path)
    return silhouette_path, img_path

def play_who_is_that_pokemon():
    """Main function to play 'Who's That Pokémon?'"""
    name = get_random_pokemon_name().lower()
    sprite_url =  get_random_pokemon_pic(name)
    filename = random.randint(1, 100000)
    silhouette_path, img_path = create_silhouette(sprite_url, filename)

    silhouette = Image.open(silhouette_path)
    out_silhouettte = silhouette.resize((600, 600))
    out_silhouettte.show()

    guess = input("Who's that Pokémon? ").lower()

    original = Image.open(img_path)
    out_original = original.resize((600, 600))
    out_original.show()

    if guess == name:
        print(f"Correct! It's {name}!")

    if guess != name:
        print(f"Wrong! It's actually {name}.")

    os.remove(silhouette_path)
    os.remove(img_path)




def main():
    pokemon_cli()

if __name__ == "__main__":
    main()