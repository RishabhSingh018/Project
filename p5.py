#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letter_password=""
number_password=""
symbol_password=""
for i in range(0,nr_letters):
    letter_password=letter_password+letters[random.randint(0,len(letters)-1)]
for i in range(0,nr_numbers):
    number_password=number_password+numbers[random.randint(0,len(numbers)-1)]
for i in range(0,nr_symbols):
    symbol_password=symbol_password+symbols[random.randint(0,len(symbols)-1)]
elements_for_password=letter_password+number_password+symbol_password
print(elements_for_password)

for i in range(0,len(elements_for_password)):
    chars = list(elements_for_password)
    random.shuffle(chars)
    final_password = ''.join(chars)
print(f"Your final password is {final_password}")
    

