import json
import os
class readWriteFile:
    def readFile(file_name):
        with open(file_name, "r") as myfile:
            data = json.load(myfile)

        return data
    
    def writeFile(file_name, obj):
        with open(file_name, "w") as myfile:
            myfile.write(json.dumps(obj, indent=4))
        return None