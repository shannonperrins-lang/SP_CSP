#SP loops notes
import random

count = 1

while count<= 10:
    print(count)
    count += 1

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("duck....")
    ducks += 1 #ducks = ducks + 1
print("GOOSE!!!")
#continue : it sends you back to the beginning of the loop..

#comeplex data type
siblings = ["alex","naomi","sean","racheal"]

#must be valid data type and spaced out by ","

print(siblings[3])
#adding to list
name = input("what's your name?:")
siblings.append("name")
siblings.insert(3,"shannon")
print(siblings)
#to remove from list 
siblings.pop(3)
print(siblings)
# for loops 
for num in range (1,11,3):
    if num % 15 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

