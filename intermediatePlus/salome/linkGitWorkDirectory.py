# this script helps to import the relevant work directories for the github script


def importPath(pathName='default'):
    import sys

    if pathName == 'default':

        pathName = './thin_pipeflow_snappyHexMesh/intermediatePlus/salome/'
    sys.path.insert(1, pathName)

    print('imported sys and added',pathName,'to sys path')

class osShortcuts:

    def __init__(self):

        import os
        self.os = os

        self.l(printHelp='true')
        self.cd(printHelp='true')
        self.pwd(printHelp='true')


    def l(self,printHelp='false',pathName='./'):

        if printHelp == 'true':

            print('========================')

            print('osShortcuts.l() is a shortcut for listing directories in salome')
            print('use salomeOS.l() to list directory, or whatever you call your object name')
            print('the default pathName is this folder')
            print(' ')

        elif printHelp == 'false':

            print(self.os.listdir('./'))


    def cd(self,printHelp='false',pathName='./home'):

        if printHelp == 'true':

            print('========================')

            print('osShortcuts.cd() is a shortcut for changing directories in salome')
            print('use salomeOS.cd() to list directory, or whatever you call your object name')
            print('it is the same as typing os.chdir(pathName)')
            print(' ')

        elif printHelp == 'false':

            self.os.chdir(pathName)

        # https://linuxize.com/post/python-get-change-current-working-directory/

    def pwd(self,printHelp='false'):

        if printHelp == 'true':

            print('========================')

            print('osShortcuts.pwd() is a shortcut for printing current directory in salome')
            print('use salomeOS.pwd() to list directory, or whatever you call your object name')
            print('it is the same as typing os.getcwd()')
            print(' ')

        elif printHelp == 'false':

            print("Current working directory: {0}".format(self.os.getcwd()))


# now this function here is to help import and reload the workspace object to make life easier 

def getWorkspaceObject():

    from importlib import reload

    # importing and reloading the liveDemoCylinderClass python module
    import liveDemoCylinderClass
    reload(liveDemoCylinderClass)

    # import the meshbuilder class
    from liveDemoCylinderClass import workspace
    workspaceObject = workspace()

    return workspaceObject


def getWorkedExamplesWorkspaceObject():

    from importlib import reload

    # importing and reloading the cylinderClass python module (under worked examples)
    import cylinderClass
    reload(cylinderClass)

    # import the meshbuilder class
    from cylinderClass import workspace
    workspaceObject = workspace()

    return workspaceObject



pathName = './thin_pipeflow_snappyHexMesh/intermediatePlus/salome/'
importPath(pathName)

pathName2 = './thin_pipeflow_snappyHexMesh/intermediatePlus/salome/videoScripts'
importPath(pathName2)

pathName3 = './thin_pipeflow_snappyHexMesh/intermediatePlus/salome/workedExamples'
importPath(pathName3)

print(' ')
print('to load workspace type')
print('from linkGitWorkDirectory import getWorkspaceObject')
print('self = getWorkspaceObject()')

print(' ')
print('or if you want the worked examples one, type:')
print('from linkGitWorkDirectory import getWorkedExamplesWorkspaceObject')
print('self = getWorkedExamplesWorkspaceObject()')
