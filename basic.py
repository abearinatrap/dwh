import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL_DELIM = "/"

url = "https://discord.com/api/webhooks/"
d_id = os.getenv('WEBHOOKID')
if d_id is None:
    print("WEBHOOKID missing from .env file")

d_token = os.getenv("WEBHOOKTOKEN")
if d_token is None:
    print("WEBHOOKTOKEN missing from .env file")

final_url=url+d_id+URL_DELIM+d_token

snddata = {'content':'info', 'username':'basicpy'}
result = requests.post(final_url, json = snddata)

print(result.status_code)