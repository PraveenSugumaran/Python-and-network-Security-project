import hashlib
character=input("Enter the character :")
character='a'+character
character=character+'b'
print(character)


#md5
H=hashlib.md5(character.encode())
print("The hasded equivalent of input is : ", end ="")
print(H.digest())

#sha224
H1=hashlib.sha224(character.encode())
print("The hasded equivalent of input is (sha224 method) : ", end ="")
print(H1.digest())

#sha1
H2=hashlib.sha1(character.encode())
print("The hasded equivalent of input is (sha1 method) : ", end ="")
print(H2.digest())

#sha512
H3=hashlib.sha512(character.encode())
print("The hasded equivalent of input is (sha512 method) : ", end ="")
print(H3.digest())

#iteration
for i in range(4):
    H = hashlib.md5(character.encode())

print("The hasded equivalent of input is (iterated for using MD5) : ", end ="")
print(H.digest())
