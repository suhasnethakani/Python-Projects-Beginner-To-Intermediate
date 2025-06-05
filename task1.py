import random
print("Welcome to Number Guessing Game")
print("Enter the number between 1-10")
print("You Have 3 Chances, So give it your best shot!!!!")
secret_number=random.randint(1,10)
chances=3
for i in range(1,chances+1):
    try:
        print("\nThis your chance number ",i)
        s=int(input("Enter a number "))
        if s==secret_number:
            print("\nYES, YOU ARE CORRECT AND THE ANSWER IS ",s)
            break
        elif s<secret_number:
            print("\nYOUR NUMBER IS LOWER THAN THE SECRET NUMBER")
        else:
            print("\nYOUR NUMBER IS HIGHER THAN THE SECRET NUMBER")
    except ValueError:
        print("Please enter a number between 1-10")
if s!=secret_number:
    print("Hard luck!!!")
    print("Your chances are done....")
    print("The Secret Number is ",secret_number,"Better luck next time")