#done
import time
from json import JSONDecodeError
from random import randint

import pygame
import requests
from io import BytesIO


from Classes.FightClass import Fight_pok
from Classes.PokemonTeamClass import PokemonTeam


def get_pokemon_sprite(name, type, mirror=False):
    """
    Fetches Sprites and also mirrors them
    :param name: Pokemon name
    :param type: Front or back sprite
    :param mirror: True or False if wanted mirrored or not
    :return: Sprite
    """
    if type == "front":
        sprite_type = "front_default"
    elif type == "back":
        sprite_type = "back_default"
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    data = response.json()


    sprite_url = data["sprites"][str(sprite_type)]

    image_data = requests.get(sprite_url).content
    image_file = BytesIO(image_data)
    sprite = pygame.image.load(image_file).convert_alpha()

    if mirror:
        sprite = pygame.transform.flip(sprite, True, False)
    sprite = pygame.transform.smoothscale(sprite, (80, 80))
    return sprite


def main():
    """
    Runs the game
    :return: Nothing
    """
    pygame.init()
    screen = pygame.display.set_mode((735, 648))
    pygame.display.set_caption("Move Your Pokémon!")
    random = randint(1,3)
    if random == 1:
        background = pygame.image.load('../Images/PokemonBackground.png').convert()
    if random == 2:
        image = pygame.image.load('../Images/img_1.png').convert()
        background = pygame.transform.smoothscale(image, (735, 648))
    if random == 3:
        image = pygame.image.load('../Images/img_2.png').convert()
        background = pygame.transform.smoothscale(image, (735, 648))

    while True:
        try:
            pokemon_name = input("Enter Pokémon to play game: ")
            sprite_front = get_pokemon_sprite(pokemon_name, "front")
            sprite_back = get_pokemon_sprite(pokemon_name, "back")
            mirrored = get_pokemon_sprite(pokemon_name, "front", True)
            if not sprite_front or not sprite_back:
                raise ValueError("Could not load sprites. Try a different Pokémon.")
            break
        except JSONDecodeError:
            print(f"Error!")



    current_sprite = sprite_front

    if current_sprite is None or sprite_back is None:
        return

    x, y = 250, 250
    speed = 4.5
    clock = pygame.time.Clock()
    start_time = time.time()
    random = randint(15,30)
    running = True
    while running:
        if time.time() - start_time >= random:
            img = pygame.image.load('../Images/img.png').convert()
            new_image = pygame.transform.smoothscale(img, (735, 648))
            screen.blit(new_image, (0, 0))
            pygame.display.flip()
            time.sleep(2)
            running = False


        screen.blit(background, (0, 0))
        screen.blit(current_sprite, (x, y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            current_sprite = sprite_front
            x -= speed
        if keys[pygame.K_RIGHT]:
            current_sprite = mirrored
            x += speed
        if keys[pygame.K_UP]:
            current_sprite = sprite_back
            y -= speed
        if keys[pygame.K_DOWN]:
            current_sprite = sprite_front
            y += speed

        clock.tick(60)

    pygame.quit()

    print("Create RED team (Player 1)")
    player_team = PokemonTeam("Player")
    for i in range(3):
        poke = input(f"Enter name for Pokémon {i + 1}: ")
        player_team.add_pokemon(poke)

    print("Create BLUE team (Player 2)")
    enemy_team = PokemonTeam("Enemy")
    for i in range(3):
        poke = input(f"Enter name for enemy Pokémon {i + 1}: ")
        enemy_team.add_pokemon(poke)

    for pok in range(0,3):
        pokemon1 = player_team.get_next_pokemon()
        pokemon2 = enemy_team.get_next_pokemon()
        if pokemon1 and pokemon2:
            battle = Fight_pok(pokemon1.pokemon, pokemon2.pokemon)

            print(battle.start_battle())
        else:
            print("No usable Pokémon to battle.")
    if battle.winsp1 > battle.winsp2:
        print("The winner is team BLUE")
    else:
        print("The winner is team RED")
main()