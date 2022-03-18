import random
import math 

lowest_number = int(input("Enter your lowest number: "))

highest_number = int(input("Enter your highest number: "))

x = random.randint(lowest_number,highest_number)



attempts = 0
too_many_tries = 5

while attempts < math.log(highest_number - lowest_number + 1,2):
    attempts += 1
    guess = int(input("What do you think the number is?: "))

    if x == guess:
        print("Congrat you scum!", attempts, "Attempts!")

        break
    
    elif x > guess:
        print(" You guessed to low")

    elif x < guess:
        print("You guessed to high")
    
    if attempts == too_many_tries:
        print("Lmao you can't even guess a number the number is: "), print(x)