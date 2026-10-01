# SP, functions notes

# write all your variables

income = float(input("what is your monthly income:"))
rent = float(input("what is your monthly rent:"))
utilities = float(input("what is your monthly utilities:"))
groceries = float(input("what is your monthly groceries:"))
transportation = float(input("what is your monthly transprtions:"))
savings = income * .1

#write any funtion you are using 

def calc_percent(income,bill):
    return round(bill/income * 100)

#outputs
print(f"your rent is ${rent:.2f} that is {calc_percent(income,rent)}% of your income.")
print(f"your utilities is ${utilities:.2f} that is {calc_percent(income,utilities)}% of your income.")
print(f"your groceries is ${groceries:.2f} that is {calc_percent(income,groceries)}% of your income.")
print(f"your transportation is ${transportation:.2f} that is {calc_percent(income,transportation)}% of your income.")