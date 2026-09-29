#SP number information

for number in range (1,21):
    if number % 2 == 0:
        if number % 5 == 0:
            print(number,"is even and is divisible by 5")
    else:
        print(number,"is odd and not divisble by 5")
    if number % 5 != 0:
        if number % 2 == 0:
            print(number,"is even and not divisble by 5")
        else:
            print(number,"is odd and not dicisble by 5")
    if number % 5 == 0:
        if number % 2 != 0:
            print(number,"is odd and divisble by 5")
        else:
            print(number,"is odd and not divisble by 5")