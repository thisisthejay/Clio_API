import requests
import json

import requests

url = "https://app.clio.com/api/v4/communications.json"


headers = {
    'Authorization': "Bearer sFlmAWzWuqMWsICFEUGt9cAwsFSRSNtcqFnm2tAN",
    'Content-Type': "application/json",
    'X-BULK': "True",
    'cache-control': "no-cache"
    }


def run_request(pld):
    starter = 0

    ender = 200


    for req in range(0,1):
        print("Request Number", req)
        payload = jsondat["data"][starter:ender]
        #print('PAYLOAD', payload, '\n\n')

        jsonified = {"data": payload}
        j_dump = json.dumps(jsonified)
        #print(j_dump)

        #print("JSONIFIED PAYLOAD: ", j_dump, '\n\n')

        print('Payload Start: ', starter)
        print('Payload End: ', ender)
        print('Payload Length:', len(payload))

        response = requests.post(url, json.dumps(jsonified), headers=headers, verify=False)

        print(response.status_code)
        print(response.content)
        print(response.reason)
        print(response.text)
        print(response.json)
        print(response.headers)

        ###### Response Log
        with open('reqerror.json', 'w') as errfile:
            json.dump(response.text, errfile)
            ######

            ###### JSONified Payload Log
        with open('jsonerror.json', 'w') as errfile:
            json.dump(jsonified, errfile)
            ######

        starter += len(payload)
        ender += len(payload)

with open('outjson_Lind.json') as f:
    jsondat = json.load(f)

    first_batch = jsondat['data'][0:10000]
    second_batch = jsondat['data'][10000:]



run_request(first_batch)
#run_request(second_batch)


