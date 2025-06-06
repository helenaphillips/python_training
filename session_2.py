import random
import math
import datetime

# fruit = input("What fruit do you like? ")
# veg = input("what veg do you like? ")
# print("you like {} and you like {}".format(fruit, veg))

# friends = input("How many friends do you have? ")
# # print(type(friends))
# pizzas = int(friends) * 0.5
# print (f'You should order {pizzas} pizzas for {friends} friends')

# now = datetime.datetime.now()
# print(now)

# for bananas in range(5):
#     print(bananas)
#
# for character in 'Banana':
#     print(character)

# for name in ['Mary', 'Fatima']:
#     print(name)
#
# for number in range(5):
#     print("executing FOR LOOP - run No {}".format(number))

#for LOOP
# total = 0
# print("*** This statement is OUTSIDE THE LOOP")
# print("Before the loop executes, our TOTAL is equal to  = ", total, '\n')
# print("--------------------------------------------------------")
#
# for number in range(3): # remember --> 0, 1, 2
#
#     print("This is loop execution for digit: " + str(number) + " inside the loop \n")
#     print("Updating total... (+ 1) \n")
#
#     total  = total + 1 # every time the loop executes, we add 1 to the total
#
#
# print("--------------------------------------------------------")
# print("***This statementWe is OUTSIDE the loop now")
# print("The final TOTAL value is: " + str(total))

# # while LOOP
# store_capacity = 5  #
# while store_capacity > 0:
#    print('Please come in. Spaces available: ' + str(store_capacity))
#    store_capacity =  store_capacity - 1
# print("\nPlease wait for someone to exit the store.")
#
# # FUNCTION
# def hello(name, pet):
#     print('Hello', name, 'and', pet)
#
# hello('Emily', 'Mr Whiskers')
# hello('Helena', 'Budgie')

# for number in range(100):
#     output = 'o' * number
#     print(output)
#
def calculate_vat(amount):
    total = amount * 1.2
    print(round(total))
calculate_vat(100)
