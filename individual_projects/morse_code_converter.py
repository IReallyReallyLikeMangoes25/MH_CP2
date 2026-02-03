# MH 2nd, morse code/english converter

# tuple for english alphabet
# tuple for morse code alphabet
english = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
morse_code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

# function to convert morse code to english, takes in a code:
def code_to_english(code, code_alphabet, english_alphabet):
    decoded = []
    # loops over sequences in the code, if the sequence is in morse code it finds the corresponding sequence in english and adds it to a list
    for sequence in code:
        if sequence == " ":
            decoded.append(" ")
        else:
            decoded.append(english_alphabet[code_alphabet.index(sequence)])
    # once the list is done convert it to a string and return the string
    decoded = "".join(decoded)
    return decoded

# function to convert english to morse code, takes in a message:
def english_to_code(message, code_alphabet, english_alphabet):
    encoded = []
    # loops over characters the message, if the character is in english it finds the corresponding sequence of code and adds it to a list
    for letter in message:
        if letter == " ":
            encoded.append(" ")
        else: 
            encoded.append(code_alphabet[english_alphabet.index(letter)])
    # once the list is done convert it to a string and return the string
    encoded = "/".join(encoded)
    return encoded

# function to check if an english input is valid
def check_input(message, alphabet):
    valid = True
    # loops over input making sure that there is nothing besides letters and spaces
    for character in message:
        if character == " ":
            pass
        elif character not in alphabet:
            valid = False
    return valid

# menu function:
def main():
    print("Welcome to the morse code encoder and decoder. Here are some quick instructions:\n1. When translating into morse code do not add punctuation, numbers, or specials characters to your sentence\n2. When translating from code to English, do not form the letters out of anything but dots (.) or dashes (-)\nThat is all, please enjoy your use of this program.")
    while True:
        # ask user what they want to do
        what_to_do = input("What do you want to do?\n1. Encode a Message\n2. Decode a Message\n3. Quit\n")
        # if they want to encode a message run the english to code function
        if what_to_do == "1":
            while True:
                convert_to_code = input("Please input your message to encode:\n").upper().strip()
                if check_input(convert_to_code, english) == False:
                    print("That is not a valid sentence. Please do not include numbers or special characters.")
                    continue
                else:
                    print(f"This message in morse code is: {english_to_code(convert_to_code, morse_code, english)}")
                    break
        # if they want to decode a message run the code to english function
        elif what_to_do == "2":
            while True:
                convert_to_english = input("Please input the code to translate with a / in between letters and spaces:\n")
                convert_to_english = convert_to_english.split("/")
                if check_input(convert_to_english, morse_code) == False:
                    print("That is not a valid code. Please only input dots, dashes, spaces, and slashes.")
                    continue
                else:
                    print(f"This message in English is: {code_to_english(convert_to_english, morse_code, english)}")
                    break
        elif what_to_do == "3":
            break
        else:
            print("That is not an option.")

main()