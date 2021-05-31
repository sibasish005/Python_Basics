import random
print("Enter 1 if You Want To Create 4 Digit PASSWORD")
print("Enter 2 if You Want To Create 6 Digit PASSWORD")
print("Enter 3 if You Want To Create 8 Digit PASSWORD")
user = int(input("Enter Your Number: "))
if user == 1:
    randomno = random.randint(1000,9999)
    print(f"Your PASSWORD is Created {randomno}")
elif user == 2:
    randomno = random.randint(100000,999999)
    print(f"Your PASSWORD is Created {randomno}")
elif user == 3:
    randomno = random.randint(10000000,99999999)
    print(f"Your PASSWORD is Created {randomno}")  
else:
    print("Enter a Valid No. 1 or 2 or 3")   