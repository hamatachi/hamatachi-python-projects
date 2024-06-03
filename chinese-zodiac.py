def get_chinese_zodiac(year):
    # Dictionary mapping remainders to Chinese Zodiac animals
    zodiac_animals = {
        0: "Monkey",
        1: "Rooster",
        2: "Dog",
        3: "Pig",
        4: "Rat",
        5: "Ox",
        6: "Tiger",
        7: "Rabbit",
        8: "Dragon",
        9: "Snake",
        10: "Horse",
        11: "Goat"
    }
    
    # Calculate the remainder
    remainder = year % 12
    
    # Get the corresponding zodiac animal
    return zodiac_animals[remainder]

# Prompt the user to enter their birth year
birth_year = int(input("Please enter your birth year: "))

# Get the corresponding Chinese Zodiac animal
zodiac_animal = get_chinese_zodiac(birth_year)

# Output the result
print(f"Your Chinese zodiac is {zodiac_animal}")
