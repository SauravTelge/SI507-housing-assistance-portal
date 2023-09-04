import json
with open('tree_./json_files/crimes.json','r') as myfile:  
            data = json.load(myfile)  
            print(data)