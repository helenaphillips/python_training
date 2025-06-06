# #Reading/writing to files
# with open('people.txt'), 'w+') as text_file:
#     people = 'Joanna \nSusan \nAmina'
#
#     text_file.write(people)

# with open('todo.txt','w+') as myeditabletodolist:
#     firstitem = 'Learn to code'
#     myeditabletodolist.write(firstitem)
#
# todo_item = input("Add a new item to your to do list")
#
# with open('todo.txt', 'r') as myeditabletodolist:
#     contents = myeditabletodolist.read()
#     print(contents)
#
# with open('todo.txt','w+') as myeditabletodolist:
#     new_contents = contents + '\n' + todo_item
#     myeditabletodolist.write(new_contents)



#Session5Homework - Question1
PIP allows you to install packages and libraries created by other users. You can add new features
to your code, to improve it's efficiency. This method saves time so you don't have to develop the code for additional
features yourself. You have the comfort of knowing that the code has been developed well with no errors.
You can use these as building blocks for your code and you don't have to worry about the smaller aspects of
your software. PIP packages are easy to install, manage, and uninstall when no longer needed.

#Question2

with open('poem.txt', 'w+') as poem_file:
    poem = 'I like Python and I am not very good at poems'
    poem_file.write(poem)

#Question3
import requests
import pprint
pokemon_number = [7,4,6,8,3,2]
with open('pokemons.txt', 'w+') as pokemon_file:
    for pokemon in pokemon_number:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
        response = requests.get(url)
        print(response)
        data = response.json()
        name = data["name"]
        pokemon_file.write('\n'+'Pokemon: '+name)
        moves = pprint.pformat(data["moves"])
        pokemon_file.write('\n'+'Moves: '+moves)

