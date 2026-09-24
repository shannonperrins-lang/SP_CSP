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