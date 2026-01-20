import random
def age_guesser():
    print("Hey you is it going! I am going to try and guess your age first I name your name")
    name = input("Name: ")
    guessed = False
    lower_bound = 15
    upper_bound =30
    while not guessed:
        age = random.randint(lower_bound,upper_bound)
        response = input(f"Is your age {age} 'y' or 'n'")
        if response == 'y':
            guessed = True
            print(f"{name} is {age} years old.")
        else:
            print("Rats")
            bound = input(f"Is the number less than or greater than {age}")
            if bound == "less than":
                upper_bound = age -1
            elif bound == "greater than":
                lower_bound = age +1
        
        
age_guesser()