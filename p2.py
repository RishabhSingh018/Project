print("Welcome to the tip claculator!")
bill_amt=float(input("What was the total bill :$ "))
tip_amt=int(input("How much tip you want to give? 10,12,15   "))
total_bill=bill_amt+(bill_amt*tip_amt*0.01)
sharing_people=int(input("How many people to split the bill : "))
ind_amt=round(total_bill/sharing_people,2)
print(f"Each person should pay : ${ind_amt}")