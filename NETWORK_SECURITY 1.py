import hashlib
character = input("Enter the character:")
hashed_character = hashlib.md5(character.encode())
print("The hasded equivalent of input is: ",end = " ")
print(hashed_character.digest())
