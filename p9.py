import random
print('''/ _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  ''')
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
numbers = []
for i in range(1, 101):
    numbers.append(i)
computer_guess_number=numbers[random.randint(0,len(numbers)-1)]
difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty_level=="easy":
    print("You have 10 attemps to guess the number.")
    i=0
    while(i<10):
        user_guess_number=int(input("Make a guess: "))
        if user_guess_number==computer_guess_number:
            print("You guessed the number")
            break
        elif user_guess_number>computer_guess_number:
            print("Too High")
        else:
            print("Too low")
        i=i+1
else:
    print("You have 5 attemps to guess the number.")
    i=0
    while(i<5):
        user_guess_number=int(input("Make a guess: "))
        if user_guess_number==computer_guess_number:
            print("You guessed the number")
            break
        elif user_guess_number>computer_guess_number:
            print("Too High")
        else:
            print("Too low")
        i=i+1
        