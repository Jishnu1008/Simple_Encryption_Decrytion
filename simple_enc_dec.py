import random 
import string
import re


char = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = char.copy()
random.shuffle(key)

def encryption(plain_text,cipher_text):
    for letter in plain_text:
        ind = char.index(letter)
        cipher_text += key[ind]
        
    return cipher_text

def decryption(decrypt_text):
    decrypted_text = ""
    for letter in decrypt_text:
        ind = key.index(letter)
        decrypted_text += char[ind]
    print(f"Decypted Text : {decrypted_text}")

plain_text = input("Enter a text to encrypt : ")
cipher_text = ""

cipher_text = encryption(plain_text,cipher_text)
print(f"Encypted Text : {cipher_text}")
pattern = "yn"
answer = input("Do you want to decrypt a text? (Y or N) : ").lower()

while(True):
         
    if answer in pattern:
        if answer == "y":
            decrypt_text = input("Enter the text to be decypted : ")
            decryption(decrypt_text)
            exit()
        else:
            exit() 
    else:
        answer = input("Please enter a valid option (Y or N) : ").lower()
        