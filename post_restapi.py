import json 
import httpx
from rich import print as rprint

headers = {
           'Authorization': 'Bearer 7faa6b08ab3603c37ff5bccb3261045a9e7c8657da5691515dd9282218970416'}

my_url = 'https://gorest.co.in/public/v2/users'

payload = {"name":"Tung Dang",
            "gender":"male", 
            "email":"tungtel@gmail.com", 
            "status":"active"}

def post_stuff(url):
    with httpx.Client(verify= False) as client:
        response = client.post(url, headers= headers , data = payload)
        structure_response = json.loads(response.text)
        return response ,structure_response
    
result = post_stuff(url = my_url)
rprint(result)
