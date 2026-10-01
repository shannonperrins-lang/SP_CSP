#SP, period 7 caesar cipher
letter = input("would you like to (E)ecrypt or (D)ecrypt a message?:")
message = input("enter your message?:")
shift = input("how many times would you like the shift your message?:")

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
    print(F"your decrypted message is: {result}")
