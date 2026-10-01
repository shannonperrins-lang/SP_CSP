#SP, period 7 caesar cipher
suggested_output = input("would you like to (E)ecrypt or (D)ecrypt a message?:")
message = input("enter your message?:")
shift = input("how many times would you like the shift your message?:")

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
    print(F"your decrypted message is: {result}")
