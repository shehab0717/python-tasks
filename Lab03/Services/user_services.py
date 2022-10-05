


from pyclbr import Function
import FileHandler.fileHandler as fileHandler
from time import time

fileHeader = ('id','first name', 'last name', 'email', 'password', 'phone number')


def insertUser(user: dict):
    user['id'] = int(time())
    row = fileHandler.toRow(user.values())
    success = fileHandler.write('user.txt', fileHeader, row)
    if success:
        return success, user
    return False, -1

def search(rule: Function):
    return fileHandler.find('user.txt',rule)