import json

class mydict(dict):
    def __str__(self):
        return json.dumps(self)

file = 'orig.json'

with open(file) as f:
    jsondat = json.load(f)

json_out = {"data": []
}
for each in jsondat:
    write_obj = {                
        "id": int(each["Matter"])       
    }

    if each["Originating_Attorney"] != None:
        write_obj["originating_attorney"] = {
            "id": int(each["Originating_Attorney"])
        }
    
    if each["Responsible_Attorney"] != None:
            write_obj["responsible_attorney"] = {
                'id': int(each["Responsible_Attorney"])
            } 


    json_out["data"].append(write_obj)

out = mydict(json_out)

#print(json_out)

with open("outjson_Lind.json", 'w') as outfile:
    json.dump(out, outfile, indent=4)


print("LENGTH: ", len(json_out['data']))
print("CALLS: ", len(json_out['data']) / 200)
#print(out)
