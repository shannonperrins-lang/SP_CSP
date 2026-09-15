# SP fixing user inputs

while True:
    color = input("tell me a color: ").strip().lower()
    if color.isnumeric():
        print("that is a number not a color!")
    elif ' ' in color:
        print("i said one word.")
else:
    break

print(f"we painted the walls {color}!")