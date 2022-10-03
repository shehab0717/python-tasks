
"""
First name
• Last name
• Email
• Password
• Confirm password
• Mobile phone

"""

from email.policy import default
import Validation.validation as vf


fields = (["first name", vf.validString],
          ["last name", vf.validString],
          ["email", vf.validateEmail], 
          ["password", vf.validatePasswrd], 
          ["confirm password", vf.validateConfirmPassword], 
          ["phone number", vf.validatePhone])


def register():
    userData = dict()
    for field in fields:
        validationFunction = field[1]
        fieldName = field[0]
        value = None
        if fieldName == "confirm password":
            value = validationFunction(password = userData["password"], message = f"{fieldName} > ")
        else:
            value = validationFunction(message = f"{fieldName} > ")
        userData[fieldName] = value

    

def start():
    print("""--------- Welcome to fundraising system ----------------
1- Login
2- Register""")
    option = input("#> ")
    match option:
        case "1":
            register()
        case "2":
            register
        case "3":
            exit()
        case _:
            start()
