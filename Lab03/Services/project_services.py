

from pyclbr import Function
import FileHandler.fileHandler as fileHandler

fileHeader = ('id', 'userId', 'title', 'details',
              'target', 'start date', 'end date')

fileName = 'project.txt'

def insert(project: dict):
    line = fileHandler.toRow(project.values())
    return fileHandler.write(fileName, fileHeader, line)

def getAll(userId):
    def rule(data):
        return data['userId']==userId
    return fileHandler.findAll(fileName, rule)

def find(rule: Function):
    return fileHandler.find(fileName, rule)
    
