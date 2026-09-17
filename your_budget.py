#SP your budget

while True:
    try:
        Income = float(input ("what is your monthly income?:"))
        break
    except:
        print("please enter a valid number for your income")

while True:
    try:
        rent = float(input ("what's your monthly rent?:"))
        break
    except:
        print("please enter a valid number for your rent")

while True:
    try:
        utilities = float(input("what's your monthly untilities bill?:"))
        break
    except:
        print("please enter a valid number for your utilities bill")

while True:
            try:
                groceries = float(input("how much do you spend on groceries a month?:"))
                break
            except:
                print("please enter a valid number for your monthly groceries")

while True:
    try:
        transprotions = float(input("how much do you spend on transportantion a month?:"))
        break
    except:
        print("please enter a valid number for your month;y transportantion")

print(f"your rent is ${rent:.2f} and that is {int(rent/Income*100)}")

print(f"your utilities is ${utilities:.2f} and that is {int(utilities/Income*100)}")

print(f"your groceries is ${groceries:.2f} and that is {int(groceries/Income*100)}")

print(f"your transprotions is ${transprotions:.2f} and that is {int(transprotions/Income*100)}")

print(f"you should save ")