# InforcePythonTask

# Registration and Authentication, Authorization


In order to log in, the user needs to send a POST request specifying the 
access key in the Authorization JWT field in the Headers and specifying 
the username and password in the body of the request.


GET TOKEN:
In order to receive a JWT token, you need to send a POST request using 
url = 'http://127.0.0.1:8000/api/v1/token/' and specify the two values 
​​username and password in the request body

Example:

url = "http://127.0.0.1:8000/api/v1/token/"

payload = {'username': 'user',
'password': '1111'}
files=[

]

headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

after that y get JSON file with refresh key and access key.

REGISTRATION:
To register a user, you need to send a POST request with the following fields 
in the request body: username, password, first_name, last_name.

Example:

url = "http://localhost:8000/api/v1/register/"

payload = {'username': 'user',
'password': '1111',
'first_name': 'Rostyk',
'last_name': 'Hereha'}
files=[]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

After that, you will get a JSON file like this:

{
    "user": {
        "id": 3,
        "password": "pbkdf2_sha256$600000$WqwxOFYYXHngktectIM3P0$ZhRTBvogMSu+0VwKDlDtO9qg8PvVPCHuCf24V8F6k1E=",
        "last_login": null,
        "is_superuser": false,
        "username": "user1",
        "first_name": "Rostyk",
        "last_name": "Hereha",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2023-07-10T22:25:00.864116Z",
        "groups": [],
        "user_permissions": []
    },
    "message": "User Created Successfully.  Now perform Login to get your token"
}


DESCRIPTION OF MAIN FUNCTIONALITY:
When creating a user to create a model in the Order table with their user_id and dish_id being null and the day of the week.
