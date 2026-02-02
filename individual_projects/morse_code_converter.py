# MH 2nd, morse code/english converter

# tuple for english alphabet
# tuple for morse code alphabet
english = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
morse_code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

# function to convert morse code to english, takes in a code:
def code_to_english(code, code_alphabet, english_alphabet):
    decoded = ""
    # loops over sequences in the code, if the sequence is in morse code it finds the corresponding sequence in english and adds it to a list
    for seqeunce in code:
    # if the given character is not in morse code print that the sentence to decode is not valid
        if sequence in code_alphabet:
            decoded.extend(english_alphabet[code_alphabet.index(sequence)]
    # once the list is done convert it to a string and return the string

# function to convert english to morse code, takes in a message:
    # loops over characters the message, if the character is in english it finds the corresponding sequence of code and adds it to a list
    # if the given character is not in english print that the sentence to encode is not valid
    # once the list is done convert it to a string and return the string


# menu function:
    # ask user what they want to do
    # if they want to encode a message run the english to code function
    # if they want to decode a message run the code to english function
