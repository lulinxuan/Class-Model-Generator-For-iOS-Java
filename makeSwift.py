import xml.etree.ElementTree

def getType(field):
    type = field.get('type')
    if type == 'boolean':
        return 'Bool'
    try:
        collection = field.get('collection')
        if collection == 'array':
            return '['+type.title()+']'
        if collection == 'set':
            return 'Set<'+type.title()+'>'
    except Exception:
        pass

    return type.title()

def getVariable(f, xmlElement):
    for field in xmlElement.findall('field'):
        varType = getType(field)
        f.write('    var '+field.get('name')+' = '+varType+'()\n')

def getGetterAndSetter(f, xmlElement):
    for field in xmlElement.findall('field'):
        varType=getType(field)
        varName=field.get('name')
        f.write('    func set'+varName.title()+'('+varName+':'+varType+'){\n')
        f.write('        self.'+varName+'='+varName+'\n')
        f.write('    }\n\n')
        
        f.write('    func get'+varName.title()+'()'+'->'+varType+'{\n')
        f.write('        return self.'+varName+'\n')
        f.write('    }\n\n')


def getToDict(f, xmlElement):
    f.write('    func toDict()->Dictionary<String, String>{\n')
    f.write('        var dict = Dictionary<String, String>()\n')
    for field in xmlElement.findall('field'):
        if field.get('collection') is not None:
            continue
        
        name=field.get('name')
        if(field.get('type') == 'Date'):
            f.write('        dict[\"'+name+'\"] = String(Int(self.'+name+'.timeIntervalSince1970))\n')
        else:
            f.write('        dict[\"'+name+'\"] = String(self.'+name+')\n')
    f.write('        return dict\n')
    f.write('    }\n')

def getConstructor(f, xmlElement):
    f.write('    init(dict:Dictionary<String, String>){\n')
    for field in xmlElement.findall('field'):
        if field.get('collection') is not None:
            continue

        name=field.get('name')

        if(field.get('type') == 'Date'):
            f.write('        self.'+name+' = Date(timeIntervalSince1970: Double(dict[\"'+name+'\"]!)!)\n')
        elif(field.get('type') == 'String'):
            f.write('        self.'+name+' = dict[\"'+name+'\"]!\n')
        else:
            f.write('        self.'+name+' = '+getType(field)+'(dict[\"'+name+'\"]!)!\n')
    f.write('    }\n\n')



def createSwiftModel(modelName, prefix, path, xmlElement):
    f=open(prefix+'/'+path+'/'+modelName+'.swift', 'w')
    f.write('\nimport UIKit\n')

    f.write('\n\n')
    
    f.write('class '+modelName+'{\n\n')
    getVariable(f, xmlElement)
    f.write('\n\n')
    
    f.write('    init(){}\n\n')

    getConstructor(f, xmlElement)
    getGetterAndSetter(f, xmlElement)
    
    getToDict(f, xmlElement)
    f.write('}\n')
    f.close()
