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
To access the daily menu, you need to make a GET request for url="http://127.0.0.1:8000/api/v1/daily/"
and send the access key in the request headers

Example:
url = "http://127.0.0.1:8000/api/v1/daily/"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDg1Mzg3LCJpYXQiOjE2ODkwODUwODcsImp0aSI6ImViMTcxYTNiYTVkYzRiZTdiODAyZjQ3NTI4YjU5M2ZmIiwidXNlcl9pZCI6MTJ9.QPSzSeAh6SH-RiHxDAyQzFdjkk045R1f_oiFZYwYCxM'
}

response = requests.request("GET", url, headers=headers, data=payload)

To access all menu items, you need to make a GET request for url="http://127.0.0.1:8000/api/v1/menulist/" and send the access key in the request headers

Example:
url = "http://127.0.0.1:8000/api/v1/menulist/"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDg1Mzg3LCJpYXQiOjE2ODkwODUwODcsImp0aSI6ImViMTcxYTNiYTVkYzRiZTdiODAyZjQ3NTI4YjU5M2ZmIiwidXNlcl9pZCI6MTJ9.QPSzSeAh6SH-RiHxDAyQzFdjkk045R1f_oiFZYwYCxM'
}

response = requests.request("GET", url, headers=headers, data=payload)

To choose a dish from the daily menu, you need to make a PUT request to 
url="http://127.0.0.1:8000/api/v1/choice/"
with access keys in the headers and id of the chosen dish in the body of the request.

Example:
url = "http://localhost:8000/api/v1/choice/"

payload = {'dish': '6'}
files=[]
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDg1NzIwLCJpYXQiOjE2ODkwODU0MjAsImp0aSI6ImY0YzMzMWI1MDE2MzRhMjlhM2QwMWUwNjRiMzVkZTNiIiwidXNlcl9pZCI6MTJ9.OZ4IM4VOV4jtWCRP--hv6aPrWyZFoEjvk6CEyL14YVE',
  'Version': ''
}

response = requests.request("PUT", url, headers=headers, data=payload, files=files)



FOR STAFF:
To get a list of selected dishes for today, you need to make GET requests to url="http://127.0.0.1:8000/api/v1/dailyrequest/" 
with access keys in the headers (admin only)


Example:
url = "http://127.0.0.1:8000/api/v1/dailyrequest/"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDg2MDczLCJpYXQiOjE2ODkwODU3NzMsImp0aSI6IjA5YWUyNmI1MzgyZTRmYzU4NTJiMmQ3OGY0MmI4YmY0IiwidXNlcl9pZCI6MX0.iyGtnkxMjcBvpvHuhVR4A7s4nJYgOgCeszybJmW9NSY'
}

response = requests.request("GET", url, headers=headers, data=payload)

At the expense of version control, I didn't have time to finish them correctly, so I just made two api urls that process data differently without checking the version in the request.



