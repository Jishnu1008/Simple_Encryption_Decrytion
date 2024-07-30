import random 
import string
import time

# Creates a char list and randomly generated key list
# This helps to map the char list to key list and substitute the letter in the given text

char = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = char.copy()
random.shuffle(key)

# Encrytion

def encryption(plain_text,cipher_text):
    for letter in plain_text:
        ind = char.index(letter)
        cipher_text += key[ind]
        
    return cipher_text

# Decryption

def decryption(decrypt_text):
    decrypted_text = ""
    for letter in decrypt_text:
        ind = key.index(letter)
        decrypted_text += char[ind]
    time.sleep(0.5)
    print(f"Decypted Text : {decrypted_text}")
    
# User is prompted to give the text to be encrypted
time.sleep(0.5)
plain_text = input("Enter a text to encrypt : ")
cipher_text = ""

cipher_text = encryption(plain_text,cipher_text)
time.sleep(0.5)
print(f"Encypted Text : {cipher_text}")
pattern = "yn"

# User is prompted to whether to decrypt or not  
time.sleep(0.5)
answer = input("Do you want to decrypt a text? (Y or N) : ").lower()

# This is to make sure that the user is pressing the correct characters

while(True):
         
    if answer in pattern:
        if answer == "y":
            time.sleep(0.5)
            decrypt_text = input("Enter the text to be decypted : ")
            decryption(decrypt_text)
            time.sleep(0.5)
            exit()
        else:
            exit() 
    else:
        answer = input("Please enter a valid option (Y or N) : ").lower()
        time.sleep(0.2)
        