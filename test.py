import requests

url = "http://127.0.0.1:5000/api/3/action/package_create"

payload = {'name': 'dataset326',
'owner_org': '111111111'}
files=[]
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': '450d85fe-78a6-4928-8446-4f1b8af7025b'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

for res in response:
    package_id=res.result.id
    print(package_id)
