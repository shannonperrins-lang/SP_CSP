#SP number information

for number in range (1,21):
    if number % 2 == 0:
        if number % 5 == 0:
            print(f"{number}is even and is divisible by 5")
        else:
            print(f"{number}is even and not divisble by 5")
    else:
        if number % 5 == 0:
            print(f"{number} is odd and is divisible by 5")
        else:
            print(f"{number} is odd and is not divisible by 5")
