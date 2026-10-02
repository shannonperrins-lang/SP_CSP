#SP, period 7 caesar cipher
letter = input("would you like to (E)ecrypt or (D)ecrypt a message?:")
sentence = input("enter your message?:")
shift = int(input("how many times would you like the shift your message?:"))

def ceasar_shift(text, shift_amount):
     result = ""
     for char in sentence:
          if char.isupper():
               result += char
               chr(ord(char) - ord("A") + shift + ord("A") % 26)
          elif char.islower():
               result += char
               chr(ord(char) - ord("a") + shift + ord("a") % 26)
          else:
             result += char
     return result

if letter == 'E' or letter == 'e':
     encrypted_sentence = ceasar_shift(sentence, -shift)
     print(f"your encryted message is: {encrypted_sentence}")

elif letter == 'D' or letter == 'd':
     decryted_sentence = ceasar_shift(sentence, shift)
     print(f"your decryted message is: {decryted_sentence}")
else:
     print("invalid letter. please chose 'D' or 'E'. ")