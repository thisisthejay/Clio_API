import json
import time
import requests

url = "https://app.clio.com/api/v4/communications.json"

headers = {
    'Authorization': "Bearer ",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'X-Bulk': "TRUE",
}

def patch_records(jsondat, last_record = 0):
    batch_size = 200
    total_records = len(jsondat['data'])

    batch_end = last_record + batch_size
    payload = {"data": jsondat["data"][last_record:batch_end]}
    
    print('Payload Start: ', last_record)
    print('Payload End: ', batch_end)
    print('Payload Length:', len(payload['data']))
    patch_request(payload)
        
    last_record += len(payload['data'])
    
    if last_record < total_records:
        patch_records(jsondat, last_record)

def patch_request(payload):
    response = requests.patch(url, data=json.dumps(payload), headers=headers, verify=False)
    code = response.status_code
    print("patch Response code: ", code)
    if code == 202:
        check_bulk_status(response.headers["Location"])
    else:
        with open('reqerror.json', 'w') as errfile:
            json.dump(response.text, errfile)

def check_bulk_status(url):
    response = requests.get(url, headers=headers, verify=False)
    print("Bulk status code: ", response.status)

    if response.headers["status"] == "429 Too Many Requests":
        print(response.text)
        time.sleep(10)
        check_bulk_status(url)
    elif response.headers["status"] != '429 Too Many Requests' or response.headers["status"] != "200 Ok" :
        write_errors('bulk_status_errror.json', response.text)

def write_errors(filename, errors):
    with open(filename, 'w') as errfile:
        json.dump(errors, errfile)

with open('api.json') as f:
    update = json.load(f)

patch_records(update)