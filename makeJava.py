import xml.etree.ElementTree

def getType(field):
    type = field.get('type')
    try:
        collection = field.get('collection')
        if collection == 'array':
            return 'List<'+type+'>'
        if collection == 'set':
            return 'Set<'+type+'>'
    except Exception:
        pass
    
    return type

def getDefaultValue(field):
    
    type = field.get('type')
    
    try:
        collection = field.get('collection')
        if collection == 'array':
            return 'new ArrayList<>()'
        if collection == 'set':
            return 'new HashSet<>()'
    except Exception:
        pass
    
    if type == 'String':
        return '\"\"'
    if type == 'Date':
        return 'new Date()'
    if type == 'int':
        return '0'
    if type == 'double':
        return '0.0'
    if type == 'boolean':
        return 'false'

    
    return type

def getVariable(f, xmlElement):
    for field in xmlElement.findall('field'):
        varType=getType(field)
        f.write('    private '+varType+' '+field.get('name')+' = '+getDefaultValue(field)+';\n')

def getGetterAndSetter(f, xmlElement):
    for field in xmlElement.findall('field'):
        varType=getType(field)
        varName=field.get('name')
        f.write('    public void set'+varName.title()+'('+varType+' '+varName+'){\n')
        f.write('        this.'+varName+'='+varName+';\n')
        f.write('    }\n\n')
        
        f.write('    public '+varType+' get'+varName.title()+'(){\n')
        f.write('        return this.'+varName+';\n')
        f.write('    }\n\n')

def getToDict(f, xmlElement):
    f.write('    public JSONObject toDict() throws JSONException{\n')
    f.write('        JSONObject dict = new JSONObject();\n')
    for field in xmlElement.findall('field'):
        name=field.get('name')
        if field.get('collection') is not None:
            if field.get('type') == 'String':
                f.write('        dict.put(\"'+name+'\", String.join(\"#,#\",this.'+name+'));\n')
            continue
        
        
        if field.get('type') == 'Date':
            f.write('        dict.put(\"'+name+'\", String.valueOf((int)(this.'+name+'.getTime()/1000)));\n')
        else:
            f.write('        dict.put(\"'+name+'\", String.valueOf(this.'+name+'));\n')
    f.write('        return dict;\n')
    f.write('    }\n')

def getConstructor(f, modelName, xmlElement):
    f.write('    public '+modelName+'(JSONObject dict) throws JSONException{\n')
    for field in xmlElement.findall('field'):
        name=field.get('name')

        if field.get('collection') is not None:
            if field.get('type') == 'String':
                f.write('        this.'+name+' = Arrays.asList(dict.getString'+'(\"'+name+'\").split(\"#,#\"));\n')
            continue
        
        if(field.get('type') == 'Date'):
            f.write('        this.'+name+' = new Date(((long)dict.getInt(\"'+name+'\"))*1000);\n')
        else:
            f.write('        this.'+name+' = dict.get'+getType(field).title()+'(\"'+name+'\");\n')
    f.write('    }\n\n')



def createJavaModel(modelName, prefix, path, xmlElement):
    f=open(prefix+'/'+path+'/'+modelName+'.java', 'w')
    f.write('package '+path.replace('/','.')+';\n\n')
    f.write('import java.io.Serializable;\n')
    f.write('import org.json.*;\n')
    f.write('import java.util.*;\n\n')
    
    f.write('public class '+modelName+' implements Serializable{\n\n')
    f.write('    public '+modelName+'(){}\n\n')
    getVariable(f, xmlElement)
    f.write('\n\n')
    getConstructor(f, modelName, xmlElement)
    getGetterAndSetter(f, xmlElement)
    
    getToDict(f,xmlElement)
    f.write('}\n')
    f.close()
