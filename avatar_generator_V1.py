import requests

male_avatars = ["Emery", "Eden", "Ryan", "Jameson", "Adrian", "Aidan", "Brooklynn"]
female_avatars = ["Vivian", "Leah", "Maria", "Jocelyn", "Riley", "Valentina", "Sarah"]
background_colours = {"Blue": "b6e3f4", "Purple": "c0aede", "Lilac": "d1d4f9", "Pink": "ffd5dc", "Yellow": "ffdfbf"}

# Ask for gender
while True:
    try:
        avatar_gender = int(input("Gender: Enter 0 for male or 1 for female: "))
        if avatar_gender in [0, 1]:
            break
        else:
            print("Please enter 0 for male or 1 for female.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Select avatar
def avatar_selection(gender):
    if gender == 0:
        avatar_list = male_avatars
    else:
        avatar_list = female_avatars

    print("Choose an avatar name from the following list:")
    for name in avatar_list:
        print(f"- {name}")

    while True:
        avatar_name = input("Name: ")
        if avatar_name in avatar_list:
            print(f"You have chosen: {avatar_name}")
            return avatar_name
        else:
            print("Invalid name. Please choose from the list.")


# Get selected name
selected_name = avatar_selection(avatar_gender)


# Pick a background colour
def avatar_colour():
    print("Select the avatar background colour: ")
    for key in background_colours.keys():
        print(f"- {key}")

    while True:
        colour = input("Colour: ")
        if colour in background_colours.keys():
            print(f"You have selected {colour}")
            return background_colours[colour]
        else:
            print("Invalid colour. Please choose from the list.")


# Join selected name with the background colour
name_and_colour = selected_name + "&backgroundColor=" + avatar_colour()

# Create URL
url = f'https://api.dicebear.com/9.x/pixel-art/svg?seed={name_and_colour}'


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