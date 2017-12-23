alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message = ""

message = input("Please enter your message: ")
key = int(input("Please choose a key: "))
user_choice = input("Do you want to encrypt(e) or decrypt(d) this message? ")

if (user_choice == "e"):
    for character in message:
        position = alphabet.find(character)
        new_position = (position + key)%26
        new_char = alphabet[new_position]
        new_message += new_char
    print("Your new message is:",new_message)
elif (user_choice == "d"):
    for character in message:
        position = alphabet.find(character)
        new_position = (position - key)%26
        new_char = alphabet[new_position]
        new_message += new_char
    print("Your original message is:",new_message)
else:
    print("Not a valid choice, terminating program")
    sys.exit()
