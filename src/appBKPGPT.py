from flask import Flask, jsonify, request
from heyoo import WhatsApp
import openai
import json

app = Flask(__name__)

@app.route('/webhook/', methods=['GET','POST'])
def webhook_whatsapp():
    if request.method == "GET":
        if request.args.get('hub.verify_token') == "GRMENDOZA":
            return request.args.get('hub.challenge')
        else:
            return "<h1>BAD AUTH</h1>"

    data=request.get_json()

    phoneNumber=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    message=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
    timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']

    send_message(chatGPT(question = message),phoneNumber)

    return jsonify({"status": "success"}, 200)

    
def chatGPT(question = ""):
    part1 = "sk-lQ3PhpomKiZ6XqZI5KnoT3"
    part2 = "BlbkFJj6IAd8FpQogkCVrchDpX"
    openai.api_key = part1+part2

    engine_model_gpt = "text-davinci-003"

    completion = openai.Completion.create(
        engine = engine_model_gpt,
        prompt = question,
        max_tokens = 4000,
        n = 1,
        stop = None,
        temperature = 0.3
    )

    response = completion.choices[0].text
    return response
    
    

def send_message(msg = "Hola",celPhone = ""):

    part1 = "EAACdvGAiCGEBAJoOBOrvRWpVRjeOQbiTHj5piKOZClPY5Xa8WkCyCOye9mXfZADMEftbjRJbBOI4"
    part2 = "jJjKXx51Te3oimoh9MMPpErqD5gRZCvO6S6kjq7wBEPgBhbrgwZBB1U5CPj8HROOC2hqepguBOyOlwwOeibWectzwhaVs6GYcbgNWV8hmcZA6j4t7hs6jwZAgboTDWmwZDZD"
    idNumber = "100739332996065"
    message = WhatsApp(part1+part2,idNumber)
    celPhone = celPhone.replace("521","52")
    message.send_message(msg,celPhone)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
