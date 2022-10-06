

from time import time
import auth
import Validation.validation as vf
import Services.project_services as projectServices

def updateProject():
    projectId = input("Enter the project id: ")
    return False

def deleteProject():
    projectId = input("Enter the project id: ")
    return False

def projectsMenue():
    print("1- Update\n2- Delete\n3- back")
    choice = input(" > ")
    match choice:
        case "1":
            updated = updateProject()
            if not updated:
                return projectsMenue()

        case "2":
            deleted = deleteProject()
            if not deleted:
                return projectsMenue()
        case "3":
            return
        case _:
            return projectsMenue()


def displayAllProjects(userId):
    projects = projectServices.getAll(userId)
    for project in projects:
        print(f"ID: {project['id']}\nTitle: {project['title']}\n"
              f"Details: {project['details']}\nTarget: {project['target']}\n"
              f"Start date: {project['start date']}\nEnd date: {project['end date']}\n"
              "----------------------------------------------------------------------")
    projectsMenue()
    

fields = (["title", vf.validateString],
          ["details", vf.validateString],
          ["target", vf.validateNumber],
          ["start date", vf.validateDate],
          ["end date", vf.validateDate])


def newProject(userId):
    project = dict()
    project['id'] = int(time())
    project['userId'] = userId
    for field, validator in fields:
        data = validator(message=f"{field} > ")
        project[field] = data
    success = projectServices.insert(project)
    if success:
        print('Project created successfully')
    else:
        print('Error happened!!')
    return project

authinticated = False
user = None
def app():
    global authinticated, user
    if not authinticated: 
        authinticated, user = auth.start()
    if authinticated:
        print(f"----------- welcome {user['first name']} ------------")
        print('1- New project \n2- list all projects \n3- exit')
        choice = input("> ")

        match choice:
            case "1":
                newProject(user['id'])
                app()
            case "2":
                displayAllProjects(user['id'])
                app()
            case "3":
                exit()
            case _:
                app()
    else:
        exit()


app()
