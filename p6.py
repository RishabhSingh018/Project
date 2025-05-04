logo='''          88                                                          88                        88                                 
           ""                                                          ""                        88                                 
                                                                                                 88                                 
 ,adPPYba, 88 ,adPPYYba, ,adPPYba,  ,adPPYba, 8b,dPPYba,     ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 ""     `Y8 I8[    "" a8P_____88 88P'   "Y8    a8"     "" 88 ""     `Y8 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 ,adPPPPP88  `"Y8ba,  8PP""""""" 88            8b         88 ,adPPPPP88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88,    ,88 aa    ]8I "8b,   ,aa 88            "8a,   ,aa 88 88,    ,88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 `"8bbdP"Y8 `"YbbdP"'  `"Ybbd8"' 88             `"Ybbd8"' 88 `"8bbdP"Y8 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                     88                                             
                                                                                     88                       '''
def encryption(text,n):
    alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
    encryptmsg=""
    for i in text:
        if i in alphabets:
            get_index=alphabets.index(i)
            encryptmsg=encryptmsg+alphabets[(get_index+n)%26]
        else:
            encryptmsg=encryptmsg+i
    print(encryptmsg)
def decryption(text,n):
    alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
    decryptmsg=""
    for i in text:
        if i in alphabets:
            get_index=alphabets.index(i)
            decryptmsg=decryptmsg+alphabets[(get_index-n)%26]
        else:
            decryptmsg=decryptmsg+i
    print(decryptmsg)
print(logo)
while(True):
    user_choice=input("Type 'encode' to encrypt, type' decode'to decrypt: ").lower()
    msg=input("Type your message:\n").lower()
    shift_amt=int(input("Type the shift number:\n"))
    if user_choice=="encode":
        encryption(msg,shift_amt)
    else:
        decryption(msg,shift_amt)
    user_continue=input("Type 'yes' to continue or 'no' to exit:\n").lower()
    if user_continue=="no":
        print("Thank you")
        break
    