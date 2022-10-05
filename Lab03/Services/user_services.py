


import FileHandler.fileHandler as fileHandler
from time import time


def insertUser(user):
    user['id'] = int(time())
    row = fileHandler.toRow(user)
    return fileHandler.write('user.txt',row), user['id']