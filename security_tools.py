import random   #Imports the random module

def validate_password(password):    #Defines the validate_password function
    if len(password) < 8:
        return False    #Returns False if the password is less than 8 characters long

    has_digit = False   #Sets has_digit to False
    has_letter = False  #Sets has_letter to False
    has_symbol = False  #Sets has_symbol to False

    for char in password:   #Loops for each character in password
        if char.isdigit():
            has_digit = True    #If the character is a digit, sets has_digit to True
        elif char.isupper() or char.islower():
            has_letter = True   #If the character is a letter, sets has_letter to True
        elif char == "!" or char == "£" or char == "$" or char == "%" or char == "&" or char == "_":
            has_symbol = True   #If the character is a symbol, sets has_symbol to True

    if has_digit == True and has_letter == True and has_symbol == True:
        return True #Returns True if the password contains at least one digit, one letter, and one symbol
    else:
        return False    #Returns False if the password does not contain at least one digit, one letter, and one symbol

def validate_ip(ip_address):    #Defines the validate_ip function
    if ip_address.count(".") != 3:
        return False    #Returns False if the IP address does not contain exactly 3 dots

    parts = ip_address.split(".")   #Splits the IP address into parts using the dot
    for part in parts:  #Loops for each part of the IP address
        if part.isdigit() == False:
            return False    #Returns False if the part is not a digit
        if int(part) < 0 or int(part) > 255:
            return False    #Returns False if the part is not between 0 and 255

    return True #Returns True if the IP address is valid

def generate_strong_password(): #Defines the generate_strong_password function

    new_password = ""   #Initializes new_password as an empty string

    strong_length = random.randint(10, 16)  #Generates a random length for the strong password to be between 10 and 16 characters

    """Generates a list of characters for the strong password, including at least one lowercase letter, one uppercase letter, one digit, and one symbol"""
    password_chars = [
        random.choice("abcdefghijklmnopqrstuvwxyz"),
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        random.choice("0123456789"),
        random.choice("!£$%&_")
    ]

    while len(new_password) != strong_length:  #Loops until the length of new_password is equal to strong_length
        new_password += random.choice(password_chars)    #Appends a random character from password_chars to new_password

    return new_password #Returns the generated strong password