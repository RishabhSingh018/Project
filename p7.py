print("""\
___________
                                  /
                          )_______(
                          |\"\"\"\"\"\"\"|_.-._,.---------.,_.-._  
                          |       | | |               | | \"'-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'\"\"\"---------\"\"\" '-'
                          )\"\"\"\"\"\"\"(
                         /_________\\
                       .-------------.
                      /_______________\\
""")
def winner(bid_winner={}):
    max=0
    for keys in bid_winner:
        if max<bid_winner[keys]:
            name=keys
            max=bid_winner[keys]
    print(f"The winner is {name} with the bid amount of ${max}")
bid_dict={}                 
while(True):
    name=input("What is your name?  ")
    amount=float(input("What is your bid ? $"))
    bid_dict[name]=amount
    bid_continue=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if bid_continue=="yes":
        print("\n"*100)
    else:
       winner(bid_dict)
       break

      