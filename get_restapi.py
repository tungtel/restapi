import httpx
import json
from rich import print as rprint 
headers = {'Accept': 'application/json', 
           'Content-Type': 'application/json'}
my_url = 'https://gorest.co.in/public/v2/users'

def pull_info(url):
    with httpx.Client(verify= False) as client:
        response = client.get(url , headers=  headers).text
        new_response = json.loads(response)
        return new_response
    
results = pull_info(my_url)
rprint(results)
