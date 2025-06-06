import random
import requests
import time

# ASCII ART(trophy)
win = '''
_____________
'._==_==_=_.'
.-\\:      /-.
| (|:.     |) |
'-|:.     |-'
  \\::.    /
   '::. .'
     ) (
   _.' '._
`""""""""""""""`
'''
# ASCII ART(crying)
lose = ''' 

.·´¯`(>▂<)´¯`·.   

'''
# ASCII ART(shrug)
draw = '''

¯\\_(ツ)_/¯

'''

# create list of stats
stat = ["id", "height", "weight", "hp", "attack", "defense", "special-attack", "special-defense", "speed"]


def random_pokemon():
    # Generate a random number between 1 and 151 to use as the Pokemon ID number.
    pokemon_number = random.randint(1, 151)

    # Using the Pokemon API get a Pokemon based on its ID number
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    # Create a dictionary that contains the returned Pokemon's name, id, height and weight
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
        'special-attack': pokemon['stats'][3]['base_stat'],
        'special-defense': pokemon['stats'][4]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat'],
    }


def game():
    print('POKEMON TOP TRUMPS')
    games_played = 0
    round_number = 1
    rounds = int(input('How many rounds would you like to play, between 1 and 5?\n'))
    if rounds <= 0 or rounds > 5:
        print("You entered an invalid number, please start again"), exit()

    you_win = 0
    computer_win = 0

    while games_played < rounds:
        print(f'\nROUND {round_number}')
        # Get 3 random Pokemon for the player
        my_pokemon = random_pokemon()
        my_pokemon2 = random_pokemon()
        my_pokemon3 = random_pokemon()

        # Ask the player to choose a Pokemon
        pokemon_choice = (input('Choose a Pokemon:\n' + my_pokemon['name'] + ', ' + my_pokemon2['name'] + ', or ' +
                                my_pokemon3['name'] + '?' + ' \n')).lower()

        if my_pokemon['name'] == pokemon_choice:
            my_pokemon = my_pokemon
        elif my_pokemon2['name'] == pokemon_choice:
            my_pokemon = my_pokemon2
        elif my_pokemon3['name'] == pokemon_choice:
            my_pokemon = my_pokemon3
        elif pokemon_choice != my_pokemon or my_pokemon2 or my_pokemon3:
            print("You entered an invalid name, please start again"), exit()

        print('You chose ' + my_pokemon['name'])
        time.sleep(1.0)

        # display stats for my pokemon
        print(stat[0], ":", my_pokemon[stat[0]])
        print(stat[1], ":", my_pokemon[stat[1]])
        print(stat[2], ":", my_pokemon[stat[2]])
        print(stat[3], ":", my_pokemon[stat[3]])
        print(stat[4], ":", my_pokemon[stat[4]])
        print(stat[5], ":", my_pokemon[stat[5]])
        print(stat[6], ":", my_pokemon[stat[6]])
        print(stat[7], ":", my_pokemon[stat[7]])
        print(stat[8], ":", my_pokemon[stat[8]])

        # Get a random pokemon for the opponent
        time.sleep(1.0)
        opponent_pokemon = random_pokemon()
        print('\nThe opponent chose ' + opponent_pokemon['name'])

        stat_choice = input('\nWho decides the stat choice: player or opponent?\n').lower()

        if stat_choice == 'player':
            # Ask the player which stat they want to use
            chosen_stat = input('\nChoose a stat:\n'
                                'id, height, weight, hp, attack, defense, special-attack, special-defense or speed?\n')

        elif stat_choice == 'opponent':
            # Let opponent choose the stat to compare
            print(
                "\nThe opponent is choosing one of the following stats to compare:\n"
                "id, height, weight, hp, attack, defense, special-attack, special-defense, speed")

            chosen_stat = random.choice(stat)
            print(f"\nThe opponent chose " + chosen_stat)

        time.sleep(2.0)
        # Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
        print(f'\nThe {chosen_stat} for {my_pokemon['name']} is: {my_pokemon[chosen_stat]}')
        print(f'The {chosen_stat} for {opponent_pokemon['name']} is: {opponent_pokemon[chosen_stat]}\n')

        if my_pokemon[chosen_stat] < opponent_pokemon[chosen_stat]:
            print('You lose!')
            computer_win += 1
        elif my_pokemon[chosen_stat] > opponent_pokemon[chosen_stat]:
            print('You win!')
            you_win += 1
        else:
            print('You draw!')
        games_played += 1
        round_number += 1

    time.sleep(2.0)
    print('\nEND OF GAME')

    if you_win > computer_win:
        print(win + f"After {rounds} rounds you win!\n")
    elif you_win == computer_win:
        print(draw + f"After {rounds} rounds you draw!")
    else:
        print(lose + f"After {rounds} rounds you lose\n")


game()