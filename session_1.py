# homework session 1 question 1
chairs = 15  # '15' incorrect
nails = 4
total_nails = chairs * nails
message = 'i need to buy {} nails'.format(total_nails)
# print('You need to buy {} nails'.format(message)) incorrect
print(message)

# question 2
my_name = 'Penelope'  # name was not in parameters
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# question 3
eggs = 6
boxes = 6
eggs_per_omelettes = 4
total_eggs = eggs * boxes
omelettes = total_eggs / eggs_per_omelettes
output = 'You can make {} omelettes with {} boxes of eggs'.format(omelettes, boxes)
print(output)

output = f'You can make {omelettes} omelettes with {boxes} boxes of eggs'
print(output)
