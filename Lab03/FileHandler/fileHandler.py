


from time import time

_DB = './Lab03/DB'

def write(fileName, line):
    try:
        file = open(f'{_DB}/{fileName}',"a")
    except Exception as e:
        print(e)
    else:
        file.write(line)
        file.close()
        return True
    

def writeAll(fileName, lines):
    try:
        file = open(f'{_DB}/{fileName}',"a")
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


