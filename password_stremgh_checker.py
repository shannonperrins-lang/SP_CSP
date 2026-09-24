#SP password strength checker

upper = False
lower = False
numbers = False
sybmol = False
length = False 
strength = 0
strengthstring = "null"
password = input("what's your password?:")

if len(password)>=8:
    len = True

for letter in password:
    if letter.isupper():
        upper = True

    if letter.islower():
        lower = True

    if letter.isnumeric():
        numbers= True

    if letter in "!@#$%^&*()":
        sybmol = True

if upper == True:
    strength += 1
if lower == True:
    strength += 1
if numbers == True:
    strength += 1
if sybmol == True:
    strength += 1
if length == True:
    strength += 1
if strength >= 5:
    strength = "strong" 
if strength <=3 and strength <= 5:
    Strength = "medium"
if strength <=2 and strength <= 0:
	Strength = "weak" 
print(f"at least 8 characters:" , length )
print(f"has an upper letter:" ,upper)
print(f"has a lowercase letter:" ,lower)
print(f"has a number:", numbers)
print(f"has a sybmol:", sybmol)
if strength >= 5:
    strengthstring = "strong"
elif strength >= 3 and strength <=4:
    strengthstring = "medium"
else:
    strengthstring = "weak"
print("your password strength is", strengthstring)