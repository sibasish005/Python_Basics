import random

def gamewin(com,you):
    if com == you:
        return None
    elif com == 'Rock':
        if you == 'Scissors':
            return False
        elif you ==  'Paper':
            return True
    elif com == 'Paper':
        if you == 'Scissors':
            return True
        elif you ==  'Rock':
            return False
    elif com == 'Scissors':
        if you == 'Paper':
            return False
        elif you ==  'Rock':
            return True

print("computer turn: Rock , Paper or Scissors")
randno = random.randint(1, 3)
if randno == 1:
    com = 'Rock'
elif randno == 2:
    com = 'Paper'    
elif randno == 3:
    com = 'Scissors' 
you = input("Your turn: Rock, Paper or Scissors? ")   
a = gamewin(com, you)       
print(f"Computer choose {com}")
print(f"You choose {you}")
if a == None:
    print("Match is Tie")
elif a:
    print("You Win") 
else:
    print("You Loose")       