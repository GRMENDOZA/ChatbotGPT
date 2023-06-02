import flask
from heyoo import WhatsApp

# data=request.get_json()
# #EXTRAEMOS EL NUMERO DE TELEFONO Y EL MANSAJE
# telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
# #EXTRAEMOS EL TELEFONO DEL CLIENTE
# mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
# #EXTRAEMOS EL ID DE WHATSAPP DEL ARRAY
# idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
# #EXTRAEMOS EL TIEMPO DE WHATSAPP DEL ARRAY
# timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']


msg = {'payload': {'contentType': 'INTERACTIVE', 'content': {'interactive': {'action': {'sections': [{'rows': [{'description': '', 'title': 'Mis compras', 'id': 'row1.1'}, {'title': 'Mi crédito', 'description': '', 'id': 'row1.2'}, {'title': 'Cómo solicitar tarjeta', 'id': 'row1.3', 'description': ''}, {'description': '', 'id': 'row1.4', 'title': 'Servicios post compra'}, {'description': '', 'title': 'Horarios de tienda', 'id': 'row1.5'}, {'id': 'row1.6', 'title': 'Información de Seguros', 'description': ''}, {'description': '', 'id': 'row1.7', 'title': 'Agencia de viajes'}, {'id': 'row1.8', 'title': 'Comprar a distancia', 'description': ''}]}], 'button': 'Menú'}, 'footer': {'text': 'Selecciona la opción'}, 'header': {'type': 'TEXT', 'text': 'Selecciona Menú para ver las opciones'}, 'body': {'text': '\n\n¡Hola!\n\nQué gusto saludarte 😁 Soy tu asistente virtual de Liverpool.\n\nConoce nuestro aviso de privacidad: https://bit.ly/2QRXmxE\n\nRecuerda que en cualquier momento puedes escribir *Menú* para volver al menú principal.\n\nTe puedo ayudar con lo siguiente:'}, 'type': 'LIST'}}}}

def send_message(msg=msg,celPhone = "525534596395"):

    part1 = "EAACdvGAiCGEBAJoOBOrvRWpVRjeOQbiTHj5piKOZClPY5Xa8WkCyCOye9mXfZADMEftbjRJbBOI4"
    part2 = "jJjKXx51Te3oimoh9MMPpErqD5gRZCvO6S6kjq7wBEPgBhbrgwZBB1U5CPj8HROOC2hqepguBOyOlwwOeibWectzwhaVs6GYcbgNWV8hmcZA6j4t7hs6jwZAgboTDWmwZDZD"
    idNumber = "100739332996065"
    message = WhatsApp(part1+part2,idNumber)
    celPhone = celPhone.replace("521","52")
    # message.send_message(msg,celPhone)
    # message.send_video(
    #     video="https://www.youtube.com/watch?v=K4TOrB7at0Y",
    #     recipient_id=celPhone,
    # )

    message.send_image(
        image="https://i.imgur.com/Fh7XVYY.jpeg",
        recipient_id=celPhone,
        caption = """*JEANS AMERICAN EAGLE 3746, 4 C, BLANCO*
Código de producto:
*1117173948*

Pedido entregado
*Tu fecha estimada de entrega se ha modificado. Fecha de Entrega: 21 de marzo*"""
        )

    # message.send_document(
    #     document="http://www.africau.edu/images/default/sample.pdf",
    #     recipient_id=celPhone,
    # )

    # message.send_location(
    #     lat=1.29,
    #     long=103.85,
    #     name="Singapore",
    #     address="Singapore",
    #     recipient_id=celPhone,
    # )

    # message.send_button(
    #     recipient_id=celPhone,
    #     button={
    #         "header": "Header Testing",
    #         "body": "Body Testing",
    #         "footer": "Footer Testing",
    #         "action": {
    #             "button": "Button Testing",
    #             "sections": [
    #                 {
    #                     "title": "iBank",
    #                     "rows": [
    #                         {"id": "row 1", "title": "Send Money", "description": ""},
    #                         {
    #                             "id": "row 2",
    #                             "title": "Withdraw money",
    #                             "description": "",
    #                         },
    #                     ],
    #                 }
    #             ],
    #         },
    #     },
    # )

    # message.send_reply_button(
    #     recipient_id=celPhone,
    #     button={
    #         "type": "button",
    #         "body": {
    #             "text": "This is a test button"
    #         },
    #         "action": {
    #             "buttons": [
    #                 {
    #                     "type": "reply",
    #                     "reply": {
    #                         "id": "b1",
    #                         "title": "This is button 1"
    #                     }
    #                 },
    #                 {
    #                     "type": "reply",
    #                     "reply": {
    #                         "id": "b2",
    #                         "title": "this is button 2"
    #                     }
    #                 }
    #             ]
    #         }
    #   },
    # )

send_message()