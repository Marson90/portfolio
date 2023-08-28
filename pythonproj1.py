import random
import secrets
import string

#acquire characters
letters = string.ascii_letters
digits = string.digits
specialchar = string.punctuation 

alphabet = letters + digits + specialchar 

#setting password length
pwd_length = 12
#generating password with all the characters in random order meeting a constraint
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if(any(char in specialchar for char in pwd)and 
       sum(char in digits for char in pwd)>=2):
        break
print(pwd)