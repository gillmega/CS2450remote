from math import random
def age_guesser():
    print("Hey you is it going! I am going to try and guess your age first I name your name")
    name = input("Name: ")
    guessed = False
    while not guessed:
        age = random.randint(15,30)
        response = input(f"Is your age {age} 'y' or 'n'")
        if response == 'y':
            guessed = True
            print(f"{name} is {age} years old.")
        else:
            print("Rats")
        
        