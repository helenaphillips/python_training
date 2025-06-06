import random
import requests

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
# ASCII ART(hand)
draw = '''
      __,--'''''''''''     ''''''''''--,__
     _-'              `\\    /'              `-_
   ,'                   `\\/'                   `,
  /                       `\\                     \\
 /                `\\        `\\                    \\
(                  /'\\        `\\                   )
(                /'   `\\        `,                 )
(              /'       `.       |                 )
 \\           /'           `-,__,-'                /
  \\        /'                        ___         /
   `.    /'                        ,'   `\\     .'
     \\ /'        /              ,--(      `\\  /
     /'        /'             ,'    \\       `<
    (        /'       /    ,--(      `\\       )
    (      /'       /'   ,'    \\       `\\    ,'
     `---,'       /'  ,--(      `\\       `\\-'
         (      /'  ,'    \\       `\\      )
          `---,'    (      `\\       `\\_,-'
              (      \\       `\\      )
               `---,' `\\       `\\_,-'   
                   (    `\\      )       
                    `---' `\\_,-'
'''


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
    games_played = 0
    round_number = 1
    rounds = int(input('How many game rounds would you like to play? \n'))

    you_win = 0
    computer_win = 0

    while games_played < rounds:
        print(f'\nTOP TRUMPS ROUND {round_number}')
        # Get 3 random Pokemon for the player
        my_pokemon = random_pokemon()
        my_pokemon2 = random_pokemon()
        my_pokemon3 = random_pokemon()

        # Ask the player to choose a Pokemon
        pokemon_choice = (input('Which Pokemon would you like to choose?\n ' + my_pokemon['name'] + ', ' + my_pokemon2['name'] + ', or ' +
             my_pokemon3['name'] + '?' + ' \n')).lower()

        if my_pokemon['name'] == pokemon_choice:
            my_pokemon = my_pokemon
        elif my_pokemon2['name'] == pokemon_choice:
            my_pokemon = my_pokemon2
        elif my_pokemon3['name'] == pokemon_choice:
            my_pokemon = my_pokemon3

        print('You chose ' + my_pokemon['name'])

        # Ask the player which stat they want to use
        stat_choice = input('Which stat do you want to use? \n '
                            'id, height, weight, hp, attack, defense, special-attack, special-defense or speed?\n ').lower()

        # Get a random pokemon for the opponent
        opponent_pokemon = random_pokemon()
        print('The opponent chose ' + opponent_pokemon['name'])

        # Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
        print(f'\nThe {stat_choice} for {my_pokemon['name']} is: {my_pokemon[stat_choice]}')
        print(f'The {stat_choice} for {opponent_pokemon['name']} is: {opponent_pokemon[stat_choice]}')
        if my_pokemon[stat_choice] > opponent_pokemon[stat_choice]:
            print('You win!')
            you_win += 1
        elif my_pokemon[stat_choice] < opponent_pokemon[stat_choice]:
            print('You lose!')
            computer_win += 1
        else:
            print('You draw!')
        games_played += 1
        round_number += 1
    print("END OF GAME")
    if you_win > computer_win:
        print(win + f"After {rounds} rounds you win!\n")
    elif you_win == computer_win:
        print(draw + f"After {rounds} rounds you draw!")
    else:
        print(lose + f"After {rounds} rounds you lose\n")

game()