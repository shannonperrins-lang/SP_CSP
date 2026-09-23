#SP password strength checker

characters = False
uppercase = False
lowercase = False
numbers = False
sybmol = False
length = False 
strength = 0
password = input("what's your password?:")

if len(password)>=8:
    length = True
print(len(password))

for letter in password:
    if letter.isupper():
        uppercase = True

    if letter.ischaracters():
        characters = True

    if letter.islowercase():
        lower = True

    if letter.isnumbers():
        numbers= True

    if letter in "!@#$%^&*()":
        sybmol = True

    if characters ==True:
        strength += 1
    if uppercase == True:
        strength += 2
    if lowercase == True:
        strength += 3
    if numbers == True:
        strength += 4
    if sybmol == True:
        strength += 5
    if length == True:
        strength += 6
    if strength == 5:
        strength = "strong" 
    if strength == <3 and >5:
