#SP, period 7 caesar cipher
letter = input("would you like to (E)ecrypt or (D)ecrypt a message?:")
message = input("enter your message?:")
shift = input("how many times would you like the shift your message?:")

<<<<<<< HEAD
def ceasar_shift(message_shift):
     result = " "

if letter.isalpha():
        if letter.isupper():
            start = ord("T")
        else:
            start = ord("t")

else:
        sentsence =+ letter

if letter == "E":
    result = ceasar_shift(message, shift)
    print(f"your encryted message is: {sentsence}")

elif letter == "D":
    result = ceasar_shift(message,-shift)
=======
def ceasar_shift(message_shift)
    sentsence = ""

    if letter.isalpha():
        if letter.isupper():
            start = ord("T")
        else:
            start = prd("t")

    else:
        sentsence = sentsence + letter

return result

if choice == "E":
    sentsence = ceaser_shift(message, shift)
    print(f"your encryted message is: {sentsence}")

elif choice == "D":
    result = cesar_shift(message,-shift)
>>>>>>> dd5cf1d43827b942bd3baa440b959b395849cab4
    print(F"your decrypted message is: {result}")
