import random
import string 
# print(help("string"))

char = list(" " + string.ascii_letters + string.digits + string.punctuation)
key = char.copy()

random.shuffle(key)

# Encryption

message = input("Type your message: ")
print()

encryption = ""

for letter in message:
    index = char.index(letter)
    encryption += key[index]

print(f"original message: {message}")
print(f"encrypted message: {encryption}")
print()

#Decryption

message = input("Type the encryption to translate: ")

decryption = ""

for letter in message:
    index = key.index(letter)
    decryption += char[index]

print()
print(f"original message: {message}")
print(f"encrypted message: {decryption}")