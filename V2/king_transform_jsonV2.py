import json

class mydict(dict):
    def __str__(self):
        return json.dumps(self)

file = 'phone_num.json'

with open(file) as f:
    jsondat = json.load(f)

json_out = {"data": []
}
for row in jsondat:
    write_obj = {
        "id": int(row["id"]),
        "phone_numbers": [],      
    }

    if row["Work"] != "":
        write_obj["phone_numbers"].append({
            "name": "Work",
            "number": row["Work"]
        })

    if row["Fax"] != "":
        write_obj["phone_numbers"].append({
            "name": "Fax",
            "number": row["Fax"]
        })

    if row["Home"] != "":
            write_obj["phone_numbers"].append({
            "name": "Home",
            "number": row["Home"]
        })

    if row["Mobile"] != "":
            write_obj["phone_numbers"].append({
            "name": "Mobile",
            "number": row["Mobile"]
        })
    json_out["data"].append(write_obj)

out = mydict(json_out)

#print(json_out)

with open("outjson_Lind.json", 'w') as outfile:
    json.dump(out, outfile, indent=4)


print("LENGTH: ", len(json_out['data']))
print("CALLS: ", len(json_out['data']) / 200)
#print(out)
