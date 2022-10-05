

import re


def validateString(message = "Your input > "):
    userInput = input(message)
    if userInput and  not userInput.isspace():
        return userInput
    return validateString("Please enter a valid string > ")

def validatePasswrd(message = "Your password > "):
    userInput = input(message)
    if len(userInput) < 4:
        return validatePasswrd('Your passwrd must be 4 chars at least, try again > ')
    return userInput

def validateConfirmPassword(password, message = "Confirm passwrd > "):
    confirmPassword = input(message)
    if(confirmPassword == password):
        return True
    return validateConfirmPassword(password, "Your password doesn't match > ")

def validatePhone(message = "Enter your phone number > "):
    phoneNumber = input(message)
    if len(phoneNumber) == 11 and phoneNumber.isdigit():
        return phoneNumber
    return validatePhone("Please enter a valid phone number > ")

def validateEmail(message = "Enter your email > "):
    email = input(message)
    if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
        return email
    return validateEmail("Incorrect email!! > ")

def validateNumber(message = " > "):
    number = input(message)
    if number.isdigit():
        return number
    print("Invalid number!")
    return validateNumber("Invalid number > ")


dateRegex = '^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
def validateDate(message = "date > "):
    date = input(message)
    if True:
        return date
    return validateDate("Date isn't valid > ")