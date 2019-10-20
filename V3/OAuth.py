import requests, json
import webbrowser

authorize_url = "https://app.clio.com/oauth/authorize"
token_url = "https://app.clio.com/oauth/token"

#callback url specified when the application was defined
callback_uri = "https://app.clio.com/oauth/approval"


#client (application) credentials
client_id = input('Please enter your App Key: ')
client_secret = input('Please enter your App secret: ')
#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=code'

webbrowser.open(authorization_redirect_url)

print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
authorization_code = input('code: ')

# step I, J - turn the authorization code into a access token, etc
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
print("requesting access token")
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print(access_token_response.status_code)
if access_token_response.status_code == 200:

    tokens = json.loads(access_token_response.text)
    access_token = tokens['access_token']
    print(access_token)

    f = open("Oauth.txt", "w")
    f.write(access_token)
    f.close()
else:

    'Please make sure you are entering the correct code.'

