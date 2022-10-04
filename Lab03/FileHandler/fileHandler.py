


from time import time


def write(fileName, line):
    try:
        file = open(fileName,"a")
    except Exception as e:
        print(e)
    else:
        file.write(line)
        file.close()
        return True
    

def writeAll(fileName, lines):
    try:
        file = open(fileName,"a")
    except Exception as e:
        print(e)
    else:
        file.writelines(lines)
        file.close()
        return True


def toRow(data: dict):
    row = ''
    for value in data.values():
        row+=f'{value}:'
    row = row[:-1] + '\n'
    return row


def insertUser(user):
    user['id'] = int(time())
    row = toRow(user)
    return write('./Lab03/DB/user.txt',row), user['id']