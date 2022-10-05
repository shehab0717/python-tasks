

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