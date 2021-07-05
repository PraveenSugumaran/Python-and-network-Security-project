import hashlib
character = input("Enter the character:")
#sha224
H1 = hashlib.sha224(character.encode())
print("The character hashed by the method sha224 is:",end="")
print(H1.digest())

#sha1
H2 = hashlib.sha1(character.encode())
print("The character hashed by the method sha1 is:",end="")
print(H2.digest())

#sha512
H3 = hashlib.sha512(character.encode())
print("The character hashed by the method sha512 is:",end="")
print(H3.digest())
