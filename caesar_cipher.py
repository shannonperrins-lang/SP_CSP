#SP, period 7 caesar cipher
letter = input("would you like to (E)ecrypt or (D)ecrypt a message?:").strip().capitalize()
sentence = input("enter your message?:").strip()
shift = int(input("how many times would you like the shift your message?:").strip())

def ceasar_shift(message_shift):
     the_result = ""
     if char on message:
          if char.isupper():
               the_result += (
                    chr((ord(char) - ord("A") + shift % 26 + ord("A")))
          elif char.islower():
               the_result += (
                    chr((ord(char) - ord("a") + shift % 26 + ord("a")))
          else:
             the_result += char
     return the_result

if letter == "D":
    the_result = ceasar_shift(message, shift)
    print(f"your decryted message is: {the_result}")

elif letter == "E":
    the_result = ceasar_shift(message,-shift)
     print(f"your encryted message is: {the_result}")
