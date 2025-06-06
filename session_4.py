student_names = ['Hank', 'Helena', 'Joshua', 'Mary']
count = 0
for student_name in student_names:
    count = count + 1
print(count)
#or use:
print(len(student_names))

costs = [8.30, 7.75, 12.40, 5.85]
total_cost = 0
for cost in costs:
    total_cost = total_cost + cost
    rounded_cost = round(total_cost, 2)
    print(rounded_cost)

HOMEWORK 1
shopping_list = [
 "oranges",
 "cat food",
 "sponge cake",
 "long-grain rice",
 "cheese board",
 ]
print(shopping_list[1]) #need to change to 0

HOMEWORK 2
chocolates = {
 'white': 1.50,
 'milk': 1.20,
 'dark': 1.80,
 'vegan': 2.00,
 }
choice = input('What type of chocolate are you selling? ')
if choice == 'white':
    print('This chocolate costs:',(chocolates['white']))
elif choice == 'milk':
    print('This chocolate costs:',(chocolates['milk']))
elif choice == 'dark':
    print('This chocolate costs:',(chocolates['dark']))
elif choice == 'vegan':
    print('This chocolate costs:',(chocolates['vegan']))
else:
    print('We do not sell this type of chocolate.')

#HOMEWORK 3
import random
lottery_ticket = [3, 1, 5, 2, 4, 9, 7]
wins = 0
for i in lottery_ticket:
    winning_number = random.randint(1, 10)
    print(winning_number)
    if winning_number in lottery_ticket:
        print('One match!')
        wins += 1
    else:
        print('No match')

if (wins <= 2):
    print('You win nothing')
elif wins == 3:
    print('You win £20!')
elif wins == 4:
    print('You win £40!')
elif wins == 5:
    print('You win £100!')
elif wins == 6:
    print('You win £10k!')
else:
    print('You win £1m!')

animals = [
    {'species': 'zebra', 'name': 'Penelope'},
    {'species': 'penguin', 'name': 'Jenn'},
    {'species': 'elephant', 'name': 'Harris'},
    {'species': 'flamingo', 'name': 'Florence'},
]
for i in animals:
    print(i['species')

#EMILY'S Solution
import random

ticket = [1, 7, 13, 21, 32, 43, 49]

winning_numbers = random.sample(range(1, 50), 7)

print(sorted(winning_numbers))

matched_numbers = 0
for number in ticket:
    if number in winning_numbers:
        matched_numbers += 1

print(f'Your number of matches is {matched_numbers}!')

if matched_numbers == 7:
    print('congratulations you have won £1000000')
elif matched_numbers == 6:
    print('Congratulations you have won £10000')
elif matched_numbers == 5:
    print('Congratulations you have won £100')
elif matched_numbers == 4:
    print('Congratulations you have won £40')
elif matched_numbers == 3:
    print('Congratulations you have won £20')
else:
    print('Bad luck, this is not a winning ticket')