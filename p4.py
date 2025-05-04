import random
print('''8888888ba                        88           88888888ba                                                   ad88888ba             88                                                       
88      "8b                       88           88      "8b                                                 d8"     "8b            ""                                                       
88      ,8P                       88           88      ,8P                                                 Y8,                                                                             
88aaaaaa8P' ,adPPYba,   ,adPPYba, 88   ,d8     88aaaaaa8P' ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,    `Y8aaaaa,    ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
88""""88'  a8"     "8a a8"     "" 88 ,a8"      88""""""'   ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8      `"""""8b, a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
88    `8b  8b       d8 8b         8888[        88          ,adPPPPP88 88       d8 8PP""""""" 88                    `8b 8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
88     `8b "8a,   ,a8" "8a,   ,aa 88`"Yba,     88          88,    ,88 88b,   ,a8" "8b,   ,aa 88            Y8a     a8P "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
88      `8b `"YbbdP"'   `"Ybbd8"' 88   `Y8a    88          `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88             "Y88888P"   `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                      88                                                                                                                   
                                                                      88                                                                                                                   ''')
paper=""" _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|                                             """
scissor="""         _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
                                   
                                   """
rock="""                    _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
                     
"""
game=[rock,paper,scissor]

user_choice=game[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))]
print(user_choice)
computer_choice=game[random.randint(0,len(game)-1)]
print(f"Computer chose:\n {computer_choice}")
if user_choice==computer_choice:
    print("There is a draw")
elif user_choice==""" _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|                                             """and computer_choice=="""         _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
                                   
                                   """:
    print("Computer Won")
elif user_choice=="""         _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
                                   
                                   """and computer_choice=="""                    _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
                     
""":
    print("Computer Won")
elif user_choice=="""                    _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
                     
"""and computer_choice==""" _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|                                             """:
    print("Computer Won")
else:
    print("User won")
