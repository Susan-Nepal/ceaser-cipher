# python program for encryption and decryption using ceaser cipher

# defining the function for welcome message
def welcome():
    print("Welcome to the Ceaser Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


# defining function for encrypting the message
def encrypt(message, shift_number):
    # import string module and define alphabets
    import string
    alphabets = string.ascii_uppercase

    # convert message to list
    message = list(message)

    # iterate through each character
    for i in range(len(message)):
        if message[i] == " ":  # if space is found keep it as a space
            message[i] = " "
        else:
            # shift character to right by the given shift number
            new_index = (alphabets.index(message[i]) + shift_number) % 26
            message[i] = alphabets[new_index]  # append new character of shifted position

    encrypted_message = "".join(message)  # join the message in single line
    return encrypted_message


# defining function for decrypting the message
def decrypt(message, shift_number):
    # import string module and define alphabets
    import string
    alphabets = string.ascii_uppercase

    # convert message to list
    message = list(message)

    # iterate through each character
    for i in range(len(message)):
        if message[i] == " ":  # if space is found keep it as a space
            message[i] = " "
        else:
            # shift character to left by the given shift number
            new_index = (alphabets.index(message[i]) - shift_number) % 26
            message[i] = alphabets[new_index]  # append new character of shifted position

    decrypted_message = "".join(message)  # join the message in single line
    return decrypted_message


# defining function for reading text from text file
def process_file(filename, mode):
    # prompt user for shift number
    valid = False  # set initial value of valid to false
    while not valid:
        try:
            while True:
                shift_number = int(input("What is shift number: "))
                if 0 < shift_number <= 25:
                    break
                else:
                    print("Invalid Shift")
            valid = True  # break the loop is shift number is valid
        except ValueError:
            print("Invalid Shift")

    with open(filename, "r") as file:  # open text file as file
        message = file.readlines()  # read lines from the file and store in message

    if mode == "e":
        encrypted_message = ""  # initialize encrypted message

        # iterate through each line in message    
        for line in message:
            line = line.upper()

            # iterate through each character in the line
            for char in line:
                # if character is alphabet encrypt it by calling encrypt function
                if char.isalpha():
                    encrypted_character = encrypt(char, shift_number)
                    encrypted_message += encrypted_character  # add encrypted character in encrypted message
                else:
                    # if character is non alphabet add as it is
                    encrypted_message += char
        return encrypted_message

    # decrypt the text file if decrypt mode is selected
    else:
        decrypted_message = ""  # initialize decrypted message

        # iterate through each line in message    
        for line in message:
            line = line.upper()

            # iterate through each character in the line
            for char in line:
                # if character is alphabet encrypt it by calling decrypt function
                if char.isalpha():
                    decrypted_character = decrypt(char, shift_number)
                    decrypted_message += decrypted_character  # add decrypted character in decrypted message
                else:
                    # if character is non alphabet add as it is
                    decrypted_message += char
        return decrypted_message


# defining function to check file existence
def is_file(filename):
    file_found = True  # initialize file found as True
    try:
        with open(filename, "r"):
            file_found = file_found  # if file is found return true

    except FileNotFoundError:
        file_found = not file_found  # return false if file not found
    
    except PermissionError:
        file_found = not file_found  # return false if file permission is not allowed
    
    except IOError:
        file_found = not file_found  # return false if there is problem with reading file

    except Exception as e:
        print(f"unknown error{e}")  # if any other problem arises display the error

    # return file_found
    return file_found


# defining function to write strings in text file
def write_message(message):
    # open result text file in write mode
    with open("results.txt", "w") as file:
        for line in message:  # iterate through each line
            file.write(line)  # write the line in result text file


# defining function to prompt console or file
def message_or_file():
    while True:
        filename = input("Enter filename: ")
        if not is_file(filename):
            print("Invalid filename")
            continue
        return filename


# defining enter message function to prompt user for message and mode
def enter_message():
    # prompt user for mode
    while True:
        mode = str(input("Would you like to encrypt (e) or decrypt (d): "))

        # prompt user for mode again if user mode is not valid
        if mode != "e" and mode != "d":
            print("Invalid Mode")
        else:
            break

    # prompt user to ask where they want to read file
    while True:
        console_or_file = str(input("Would you like to read from a file (f) or the console (c)?"))
        if console_or_file != "f" and console_or_file != "c":
            continue
        else:
            break
    if console_or_file == "f":
        message = ""
        shift_number = ""
    # prompt user for message to encrypt or decrypt according to mode selected by user 
    if mode == "e" and console_or_file == "c":
        while True:
            message = input("What message would you like to encrypt: ").upper()  # prompt user for input
            if all(char.isalpha() or char.isspace() for char in
                   message):  # check if user input contains any non alphabet
                break  # break the loop if all character is alphabet

    elif mode == "d" and console_or_file == "c":
        while True:
            message = input("What message would you like to decrypt: ").upper()  # prompt user for input
            if all(char.isalpha() or char.isspace() for char in
                   message):  # check if user input contains any non alphabet
                break  # break the loop if all character is alphabet

    if console_or_file == "c":
        valid = False  # set initial value of valid to false
        while not valid:
            try:
                while True:
                    shift_number = int(input("What is shift number: "))
                    if 0 <= shift_number <= 25:
                        valid = True  # break the loop is shift number is valid
                        break
                    else:
                        print("Invalid Shift")
            except ValueError:
                print("Invalid Shift")

    # return mode, message and shift number
    return mode, message, shift_number, console_or_file


# define main function 
def main():
    # call the welcome function
    welcome()
    while True:
        # call the enter_message function and store its returned value
        mode, message, shift_number, console_or_file = enter_message()

        # if mode is e call encrypt function and pass the arguments
        if console_or_file == "c":
            if mode == "e":
                encrypted_message = encrypt(message, shift_number)
                print(encrypted_message)

            else:  # else call the decrypted function and pass the argument
                decrypted_message = decrypt(message, shift_number)
                print(decrypted_message)

        if console_or_file == "f":
            filename = message_or_file()
            message = process_file(filename, mode)
            print("output written to results.txt")
            write_message(message)

        while True:
            # ask user if they want to encrypt or decrypt another message
            user = str(input("Would you like to encrypt or decrypt another message? (y/n): "))
            if user == "y" or user == "n":  # check if user input is valid
                break  
            else:
                continue  # if user input is not valid prompt again for input

        if user == "n":  # terminate the program if user input is n
            print("Thanks for using the program, goodbye!")
            break

# call the main function to run the program
main()
