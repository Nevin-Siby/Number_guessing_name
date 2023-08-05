import random

top_of_number = input("Type a number for limit:")

if top_of_number.isdigit():
    top_of_number = int(top_of_number)
    if top_of_number < 0:
        print("Enter a number greater than 0")
        quit()
else:
    print("Enter a number ,stupid")
    quit()

r= random.randint(0, top_of_number)
guesses=0

while True:
    guesses +=1
    user_guess= input("Enter your guess")
    if user_guess.isdigit():
        user_guess= int(user_guess)
        if user_guess<0:
            print("Enter a number greater than 0")
    else:
        print("Enter a number next time")
        continue
    
    if user_guess == r:
        print("You got it")
        break
    elif r>user_guess:
        print("Random number is greater than this number")
    else: 
        print("Random number is lesser than this number")
print("You got it in",guesses,"guesses")
        
    


    