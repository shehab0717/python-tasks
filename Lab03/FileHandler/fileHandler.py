
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


def write(fileName, fileHeader, line):
    if checkFile(fileName, fileHeader):
        try:
            file = open(filePath(fileName), "a")
        except Exception as e:
            print(e)
            return False
        else:
            file.write(line)
            file.close()
            return True
    return False


def writeAll(fileName, fileHeader, lines):
    if checkFile(fileName, fileHeader):
        try:
            file = open(filePath(fileName), "a")
        except Exception as e:
            print(e)
        else:
            file.writelines(lines)
            file.close()
            return True


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
    #remove \n from the row and file header
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
        return results

