import requests
from dotenv import load_dotenv
import os
import sys
import getopt
import subprocess

load_dotenv()

URL_DELIM = "/"

url = "https://discord.com/api/webhooks/"
d_id = os.getenv('WEBHOOKID')
if d_id is None:
    print("WEBHOOKID missing from .env file")

d_token = os.getenv("WEBHOOKTOKEN")
if d_token is None:
    print("WEBHOOKTOKEN missing from .env file")

USERNAME="livepy"
CONTENT_STRING=""

if __name__ == "__main__":
    argv = sys.argv[1:]

    HELP_STRING = """    -u <USERNAME> : Username the message is displayed under
    -c <CONTENT_STRING> : Content to send as webhook message
    -i : Send results from 'ifconfig' as message
    -h : Display this message"""

    try:
        opts, args = getopt.getopt(argv, "rhic:u:", ["content=", "username="])
    except getopt.GetoptError:
        print("Option error!")
        print(HELP_STRING)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print(HELP_STRING)
            sys.exit()
        elif opt in ("-c", "--content"):
            pass
        elif opt in ("-i"):
            #use if need to grep
            #result = subprocess.check_output("ifconfig", shell=True)
            result = subprocess.check_output(['ifconfig'])
            CONTENT_STRING += result.decode('UTF-8')
            #print(CONTENT_STRING)
        elif opt in ("-r"):
            result = subprocess.check_output(["curl", "ifconfig.co/"])
            CONTENT_STRING += result.decode('UTF-8')
        elif opt in ("-u", "--username"):
            USERNAME=arg
        else:
            assert False, "unhandled option"


    final_url=url+d_id+URL_DELIM+d_token

    MAX_SIZE=2000
    chunks = [CONTENT_STRING[i:i+2000] for i in range(0, len(CONTENT_STRING), MAX_SIZE)]

    for chunk in chunks:
        snddata = {'content':chunk, 'username':USERNAME}
        result = requests.post(final_url, json = snddata)

    #print(result.status_code)

    if result.status_code == 204:
        print("Success")