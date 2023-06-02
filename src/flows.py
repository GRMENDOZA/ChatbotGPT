from heyoo import WhatsApp

def welcome():
    msgToClient = """¡Hola!

Qué gusto saludarte 😁 Soy tu asistente virtual de Liverpool.

Conoce nuestro aviso de privacidad: https://bit.ly/2QRXmxE

Recuerda que en cualquier momento puedes escribir *Menú* para volver al menú principal.

Te puedo ayudar con lo siguiente:"""
    buttons = {
                "header": "Menú principal",
                "body": msgToClient,
                "footer": "Selecciona *Menú* para ver las opciones",
                "action": {
                    "button": "Menú",
                    "sections": [
                        {
                            "title": "Menú",
                            "rows": [
                                {
                                    "id": "row1",
                                    "title": "Consulta Pedido",
                                    "description": ""},
                                {
                                    "id": "row2",
                                    "title": "Consulta Saldo",
                                    "description": "",
                                },
                            ],
                        }
                    ],
                },
            }
    return buttons