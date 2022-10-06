import os.path
from pyclbr import Function


_DB = './Lab03/DB'


def filePath(fileName):
    return f'{_DB}/{fileName}'


def checkFile(fileName, fileHeader):
    if not os.path.exists(filePath(fileName)):
        try:
            file = open(filePath(fileName), 'w')
        except Exception as e:
            print(e)
            return False
        else:
            file.write(toRow(fileHeader))
            file.close()
            return True
    return True


def write(fileName, fileHeader, line, append=True):
    if checkFile(fileName, fileHeader):
        mode = "a"
        if not append: 
            mode = "w"
        try:
            file = open(filePath(fileName), mode)
        except Exception as e:
            print(e)
            return False
        else:
            file.write(line)
            file.close()
            return True
    return False


def writeAll(fileName, fileHeader, lines: list, append=True):
    if checkFile(fileName, fileHeader):
        mode = "a"
        if not append: 
            mode = "w"
        try:
            file = open(filePath(fileName), mode)
        except Exception as e:
            print(e)
        else:
            file.writelines(lines)
            file.close()
            return True
    return False

def getFileHeader(fileName):
    try:
        file = open(filePath(fileName), 'r')
    except Exception as e:
        print(e)
        return None
    else:
        header = file.readline()
        file.close()
        return header


def assignWithHeader(row, fileHeader):
    # remove \n from the row and file header
    row = row[:-1]
    fileHeader = fileHeader[:-1]
    fields = row.split(':')
    cols = fileHeader.split(':')
    data = dict()
    for i in range(len(fields)):
        data[cols[i]] = fields[i]
    return data


def find(fileName, rule):
    try:
        file = open(filePath(fileName), 'r')
    except Exception as e:
        print(e)
        return None
    else:
        lines = file.readlines()
        fileHeader = getFileHeader(fileName)
        for line in lines:
            data = assignWithHeader(line, fileHeader)
            if rule(data):
                file.close()
                return data
        file.close()
        return None


def toRow(data):
    row = ''
    for value in data:
        row += f'{value}:'
    row = row[:-1] + '\n'
    return row


def findAll(fileName, rule: Function):
    try:
        file = open(filePath(fileName), 'r')
    except Exception as e:
        print(e)
        return None
    else:
        lines = file.readlines()
        results = []
        fileHeader = getFileHeader(fileName)
        for line in lines:
            data = assignWithHeader(line, fileHeader)
            if rule(data):
                results.append(data)
        file.close()
        return results


def delete(fileName, rule: Function):
    def ruleToAll(data):
        return True
    all = findAll(fileName, ruleToAll)
    remaining = []
    for entry in all:
        if not rule(entry):
            remaining.append(toRow(entry.values()))
    return writeAll(fileName, getFileHeader(fileName), remaining, append=False)

def update(fileName, newData):
    def rule(data):
        return data['id'] == newData['id']
    deleted = delete(fileName, rule)
    if deleted:
        return write(fileName, getFileHeader(fileName), toRow(newData.values()))
    return False