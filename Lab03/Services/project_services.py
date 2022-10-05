

import FileHandler.fileHandler as fileHandler

fileHeader = ('id', 'userId', 'title', 'details',
              'target', 'start date', 'end date')

fileName = 'project.txt'

def insert(project: dict):
    line = fileHandler.toRow(project.values())
    return fileHandler.write(fileName, fileHeader, line)
