import requests
import logging
import json
import os

logger = logging.getLogger(__name__)

part1 = "EAACdvGAiCGEBAJoOBOrvRWpVRjeOQbiTHj5piKOZClPY5Xa8WkCyCOye9mXfZADMEftbjRJbBOI4jJjKXx51Te3oimoh9MMPpErqD5gRZCvO6S6kjq"
part2 = "7wBEPgBhbrgwZBB1U5CPj8HROOC2hqepguBOyOlwwOeibWectzwhaVs6GYcbgNWV8hmcZA6j4t7hs6jwZAgboTDWmwZDZD"

def getMediaUrl(id = ''):
    url = f"https://graph.facebook.com/v16.0/{id}/"
    headers = { "Authorization": "Bearer {}".format(part1 + part2) }
    try:
        response = requests.request("GET", url, headers=headers)
        resultjson = json.loads(response.text)
        msgLog = 'URL Media Success'
        logger.info(msgLog)
        return resultjson['url']
    except BaseException as error:
        msgLog = error
        logger.error(msgLog)
        return error
    

def downloadMedia(id = ''):
    url = getMediaUrl(id)
    headers = { 'Authorization': 'Bearer {}'.format(part1 + part2) }
    try:
        response = requests.request('GET', url, headers=headers)
        mediaType = response.headers['Content-Disposition'].split('.')[1]
        nameFile = f'{id}.{mediaType}'
        mediaData = open(f'../static/{nameFile}', 'wb').write(response.content)
        msgLog = 'Download Media Success'
        logger.info(msgLog)
        return nameFile
    except BaseException as error:
        msgLog = error
        logger.error(msgLog)
        return error


# downloadMedia(id = '1723118684792018')