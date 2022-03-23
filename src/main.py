import random
import math

# Where the User inputs the lowest number
lowest_number = int(input("Enter your lowest number: "))

# Where the User inputs the highest number
highest_number = int(input("Enter your highest number: "))

# Makes the range and random number
x = random.randint(lowest_number, highest_number)


# number of attempts
attempts = 0
guess = 0

# Number of attempts which will end the game
too_many_tries = round(math.sqrt(highest_number-lowest_number))


while attempts < too_many_tries and guess != x:
    print("You have " + str(too_many_tries - attempts) + " guesses.")
    attempts += 1
    guess = int(input("What do you think the number is?: "))
    if guess < x:
        print("That's too low.")
    elif guess > x:
        print("That's too high")

if x == guess:
    print("Congrat you scum!", attempts, "Attempts!")
else:
    print("Lmao you can't even guess a number the number is: "), print(x)
