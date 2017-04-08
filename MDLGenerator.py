import xml.etree.ElementTree
import os
import shutil
from makeJava import *
from makeSwift import *

root = xml.etree.ElementTree.parse('model.xml').getroot()

def createJava():
    global root
    language='java'
    rootPath='model'
    if os.path.exists(language):
        shutil.rmtree(language, ignore_errors=True)
    os.makedirs(language)
    os.makedirs(language+'/'+rootPath)

    for namespace in root.findall('namespace'):
    
        namespaceName=namespace.get('name')
        namespacePath=rootPath+'/'+namespaceName
        os.makedirs(language+'/'+namespacePath)
    
        for model in namespace.findall('model'):
            modelName=model.get('name')
            createJavaModel(modelName, language, namespacePath, model)


def createSwift():
    global root
    language='swift'
    rootPath='model'
    if os.path.exists(language):
        shutil.rmtree(language, ignore_errors=True)
    os.makedirs(language)
    os.makedirs(language+'/'+rootPath)

    for namespace in root.findall('namespace'):
    
        namespaceName=namespace.get('name')
        namespacePath=rootPath+'/'+namespaceName
        os.makedirs(language+'/'+namespacePath)
        
        for model in namespace.findall('model'):
            modelName=model.get('name')
            createSwiftModel(modelName, language, namespacePath, model)

createJava()
createSwift()
