print("Welcome to the pizza deliviers")
size=input("What size do want ? S,M or L?: ")
pepperoni=input("Do you want pepperoni on your pizza ? Y or N :")
extra_chesse=input("Do you want Extra cheese ? Y or N :")
if size=="S":
    bill=15
elif size=="M":
    bill=20
else:
    bill=25
if pepperoni=="Y":
    if size=="S":
        bill=bill+2
    else:
        bill=bill+3
if extra_chesse=="Y":
    bill=bill+2
print(f"The total amount you need to pay is ${bill}")
   
    