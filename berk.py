import requests

token = "token buraya"
url = "https://discord.com/api/v9/users/@me/invites"
headers = {'Accept': '*/*','Authorization': f'{token}'}

response = requests.post(url, headers=headers, json={})

if response.status_code == 200:
    json_response = response.json()
    code = json_response.get("code")
    print(code)
else:
    print(f"Hata: {response.status_code}")
    print(response.text)