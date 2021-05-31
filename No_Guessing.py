import random
randomno = random.randint(1,10)
guesses = 0
userguess = None
while(userguess != randomno):
    print("Guess The Number Between 1 to 10")
    userguess = int(input("Enter Your Guess: "))
    if (userguess == randomno):
        print("You Guess It Right! ")
    else:
        if (userguess > randomno):
            print("You Guess It Wrong! Please Enter Small No. ")
        else:
            print("You Guess It Wrong! Please Enter Big No ")
    guesses = guesses+1        
print(f"You Guess It Right In {guesses} Guess")