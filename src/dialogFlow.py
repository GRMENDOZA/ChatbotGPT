import requests
import json
from getToken import *

def dialogFlow():
    url = "https://dialogflow.googleapis.com/v2/projects/liv-dev-dig-chatbot/agent/sessions/8078:detectIntent"

    payload = json.dumps(
        {
    "query_input": {
        "text": {
            "text": "gustavo",
            "language_code": "es-MX"
        }
    },
    "queryParams": {
        "payload": {
            "chanel": "WHATSAPP",
            "from": "525534596395",
            "to": "524436892200",
            "conversationId": "27c4b30"
        }
    }
    }
    )

    headers = {
    'Content-Type': 'application/json',
    'Authorization': token()
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    resultjson = json.loads(response.text)

    for i in resultjson['queryResult']['fulfillmentMessages']:
        print(i)

    return resultjson['queryResult']['fulfillmentMessages']

dialogFlow()
