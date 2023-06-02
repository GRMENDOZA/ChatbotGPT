from flask import Flask, jsonify, request, send_from_directory
import logging
import re
from embedding import *
from getMedia import downloadMedia
from speechRecognition import textRecognition
from sendMessage import send_message


conocimiento = None

app = Flask(__name__)

@app.before_first_request
def load_embeddings():
    global conocimiento
    conocimiento = pd.read_csv('../database/embeddings.csv')

@app.route('/webhook', methods=['GET','POST'])
def webhook_whatsapp():
    if request.method == "GET":
        if request.args.get('hub.verify_token') == "GRMENDOZA":
            return request.args.get('hub.challenge')
        else:
            return "<h1>BAD AUTH</h1>"

    if request.method == "POST":
        data = request.get_json()
        flagData = 0
        typeMessage = ''
        caption = ''
        idMedia = ''
        idWa = ''
        timeStamp = ''
        phoneNumber = ''
        
        if 'messages' in data['entry'][0]['changes'][0]['value']:
            conocimiento = pd.read_csv('../database/embeddings.csv')
            msgLog = data
            app.logger.info(msgLog)
            flagData = 1
            message_data = data['entry'][0]['changes'][0]['value']['messages'][0]
            typeMessage = message_data.get('type')
            phoneNumber = message_data.get('from')
            idWa = message_data.get('id')
            timeStamp = message_data.get('timestamp')
            
        if typeMessage == 'text' and flagData == 1:
            message = message_data['text']['body']
            msgFlow = buscar(message, conocimiento)
            send_message_wrapper(phoneNumber, msgFlow, message)

        if typeMessage == 'interactive' and flagData == 1:
            message = message_data['interactive']['list_reply']['title']
            msgFlow = buscar(message, conocimiento)
            send_message_wrapper(phoneNumber, msgFlow, message)

        if typeMessage in ['image','video','audio'] and flagData == 1:
            media_data = message_data.get(typeMessage, {})
            caption = media_data.get('caption', '')
            idMedia = media_data.get('id')

            if typeMessage == 'audio':
                infoDownload = downloadMedia(id=idMedia)
                text = textRecognition(id=idMedia) 

                if text[1] == 1:
                    text[0] = re.sub(r'(\d)\s+(\d)', r'\1\2', text[0]).strip()
                    if text[0].replace(' ','').strip().isnumeric():
                        text[0] = text[0].replace(' ','').strip()
                    app.logger.info(text[0])
                    msg = text[0]
                    msgFlow = buscar(text[0], conocimiento)
                    app.logger.info(f'Flujo Identificado ---> {msgFlow}')
                else:
                    msg = 'Audio no reconocible, intenta nuevamente'
                    app.logger.info(msg)
                    msgFlow = 404
                send_message_wrapper(phoneNumber, msgFlow, msg)

    return jsonify({"status": "success"}, 200)


def send_message_wrapper(phone_number, flow, message):
    send_message(phone_number, flow=flow, data=message)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
