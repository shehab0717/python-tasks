import Services.user_services as userServices
import Validation.validation as vf


fields = (["first name", vf.validateString],
          ["last name", vf.validateString],
          ["email", vf.validateEmail], 
          ["password", vf.validatePasswrd], 
          ["confirm password", vf.validateConfirmPassword], 
          ["phone number", vf.validatePhone])


def register():
    userData = dict()
    userData['id'] = ''
    for field in fields:
        validationFunction = field[1]
        fieldName = field[0]
        value = None
        if fieldName == "confirm password":
            value = validationFunction(password = userData["password"], message = f"{fieldName} > ")
        else:
            value = validationFunction(message = f"{fieldName} > ")
        userData[fieldName] = value
    del userData["confirm password"]
    return userServices.insertUser(userData)
    


def login():
    email = input('email > ')
    password = input('password > ')
    def rule(userData: dict):
        return userData['email'] == email and userData['password'] == password
    user = userServices.search(rule)
    if user:
        return True, user
    return False, None

def start():
    print("""--------- Welcome to fundraising system ----------------
1- Login
2- Register""")
    option = input("#> ")
    match option:
        case "1":
            return login()
        case "2":
            return register()
        case "3":
            exit()
        case _:
            return start()
