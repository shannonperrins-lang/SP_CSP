#SP, reading and writing files

with open("7th/.practice.txt", "r+") as file: #<- how to make another file show another files content. lets you read and appending 
    content = file.read()
    content = "chapter 1:\n" + content + "and christopher robin was sitting on his doorstep putting on his big boots."
    file.write(content)

with open("7th/pratice.txt","w") as file:
    file.write("/nWinnie the Pooh and The Blustary Day") # write dealtes the rest of the other file and replaces it

with open("7th/pratice.txt","a") as file:
    file.write("\nWinnie the Pooh and The Blustary Day")
#a=apend  adds content to the end

#r+ lets you read an write