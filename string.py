#SP strings notes

#anything insaide of quotetion marks

name = input("what is your name?:").strip().lower().capitalize()

age = input("how old are you?:")

print(type(age))

print(age+age)

# concatenation => pus two strings directly next tp each other

print(name + " " + "LaRose")

#
sentece = "the quick down fox jumped over the lazy dog"

print(sentece)
print(sentece.replace("dog","monkey"))
print(len(name))#<= gets the length of a string
print(f"Your name is {name} that is {len(name)} letters long. your frist initial is {name[0]} i think i will call you {name[0:2]}")

