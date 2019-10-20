import json

class mydict(dict):
    def __str__(self):
        return json.dumps(self)

file = 'phone_num.json'

with open(file) as f:
    jsondat = json.load(f)

json_out = {"data": []
}
for each in jsondat:
    write_obj = {
        "id": int(each["id"]),
        "phone_numbers": [{
            "name": "Fax",
            "number": each["Business Fax"]
        },{
            "name": "Work",
            "number": each["Business Phone"]
        },{
            "name": "Home",
            "number": each["Home Phone"]
        },{
            "name": "Mobile",
            "number": each["Mobile Phone"]
        }],      
    }
    json_out["data"].append(write_obj)

out = mydict(json_out)

#print(json_out)

with open("outjson_Lind.json", 'w') as outfile:
    json.dump(out, outfile, indent=4)


print("LENGTH: ", len(json_out['data']))
print("CALLS: ", len(json_out['data']) / 200)
#print(out)
