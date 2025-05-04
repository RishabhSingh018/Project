print("Welcome to the python calculator")
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={"+":add,"-":sub,"*":mul,"/":div}

first_number=float(input("What is the first number: "))
while(True):
    for keys in operations:
        print(keys)
    pick_up_operation=input("pick an operation: ")
    second_number=float(input("What's the next number: "))
    result=operations[pick_up_operation](first_number,second_number)
    print(f"{first_number}{pick_up_operation}{second_number}={result}")
    user_continue=input("Type y to continue or, type 'n' to exit\n").lower()
    if user_continue=="n":
        break
    else:
        first_number=result
        
