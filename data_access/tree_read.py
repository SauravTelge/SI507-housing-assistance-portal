import json
with open('tree_crimes.json','r') as myfile:  
            data = json.load(myfile)  
            print(data)