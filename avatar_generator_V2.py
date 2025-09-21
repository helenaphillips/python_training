import random
import requests
import time

print("Avatar Builder! Customise your avatar.")
time.sleep(1.0)

# Base data
skin_colour = {"Pale": "ffdbac", "Ivory": "eac393", "Medium": "cb9e6e", "Tanned": "b68655", "Bronze": "a26d3d",
               "Espresso": "8d5524"}
hair_colour = {"Blonde": "cab188", "Light Brown": "83623b", "Dark Brown": "28150a", "Red": "bd1700", "Blue": "009bbd"}
hairstyle = {"Long": "long12", "Pigtails": "long02", "Space Buns": "long14", "Short Curls": "long15",
             "Short": "short01"}
mouth_shape = {"Happy": "happy09", "Laughing": "happy06", "Neutral": "sad06", "Sad": "sad01", "Shocked": "happy01"}
clothing_colour = {"Blue": "5bc0de", "Green": "44c585", "Red": "ae0001", "Yellow": "ffd969", "Pink": "ff6f69"}
background_colours = {"Blue": "b6e3f4", "Purple": "c0aede", "Lilac": "d1d4f9", "Pink": "ffd5dc", "Yellow": "ffdfbf"}


# Ask for skin colour
def skin_colour_choice():
    print("Pick a skin colour:")
    time.sleep(1.0)
    for i in skin_colour.keys():
        print(f"- {i}")
    while True:
        skin_choice = input("Skin colour: ")
        if skin_choice in skin_colour.keys():
            print(f"You have selected {skin_choice}")
            return "&skinColor=" + skin_colour[skin_choice]
        else:
            print("Invalid entry. Please choose from the list.")


# Ask for hair colour
def hair_colour_choice():
    print("Pick a hair colour:")
    time.sleep(1.0)
    for i in hair_colour.keys():
        print(f"- {i}")
    while True:
        hair_choice = input("Hair colour: ")
        if hair_choice in hair_colour.keys():
            print(f"You have selected {hair_choice}")
            return "&hairColor=" + hair_colour[hair_choice]
        else:
            print("Invalid entry. Please choose from the list.")


# Ask for hairstyle
def hairstyle_choice():
    print("Pick a hairstyle:")
    time.sleep(1.0)
    for i in hairstyle.keys():
        print(f"- {i}")
    while True:
        haircut_choice = input("Hairstyle: ")
        if haircut_choice in hairstyle.keys():
            print(f"You have selected {haircut_choice}")
            return "&hair=" + hairstyle[haircut_choice]
        else:
            print("Invalid entry. Please choose from the list.")


# Ask for expression
def mouth_choice():
    print("Pick an expression:")
    time.sleep(1.0)
    for i in mouth_shape.keys():
        print(f"- {i}")
    while True:
        mouth = input("Mood: ")
        if mouth in mouth_shape.keys():
            print(f"You have selected {mouth}")
            return "&mouth=" + mouth_shape[mouth]
        else:
            print("Invalid entry. Please choose from the list.")


# Ask for clothing colour
def clothing_colour_choice():
    print("Pick the clothing colour:")
    time.sleep(1.0)
    for i in clothing_colour.keys():
        print(f"- {i}")
    while True:
        clothing_choice = input("Clothing colour: ")
        if clothing_choice in clothing_colour.keys():
            print(f"You have selected {clothing_choice}")
            return "&clothingColor=" + clothing_colour[clothing_choice]
        else:
            print("Invalid entry. Please choose from the list.")


# Pick a background colour
def avatar_colour():
    print("Select the avatar background colour: ")
    time.sleep(1.0)
    for key in background_colours.keys():
        print(f"- {key}")
    while True:
        colour = input("Colour: ")
        if colour in background_colours.keys():
            print(f"You have selected {colour}")
            return "&backgroundColor=" + background_colours[colour]
        else:
            print("Invalid entry. Please choose from the list.")


# Join choices together
customisation = (skin_colour_choice() + hair_colour_choice() + hairstyle_choice() + mouth_choice() +
                 clothing_colour_choice() + avatar_colour())

# Name the avatar
selected_name = input("Finally, give your avatar a name: ")

# Create URL
url = f'https://api.dicebear.com/9.x/pixel-art/svg?seed=Maria{customisation}'


# Download and save image
response = requests.get(url)
if response.status_code == 200:
    with open(f"{selected_name}.svg", "wb") as img_file:
        img_file.write(response.content)
    print(f"Avatar image saved as {selected_name}.svg")
else:
    print("Failed to download the avatar image.")

# Create shortcut
with open(f"{selected_name}.url", "w") as shortcut:
    shortcut.write("[InternetShortcut]\n")
    shortcut.write(f"URL={url}\n")
print(f"Shortcut saved as {selected_name}.url")