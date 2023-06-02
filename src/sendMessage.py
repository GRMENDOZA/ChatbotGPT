from heyoo import WhatsApp
from flows import *
from consultaATG import * 
import re
import logging
import os

logger = logging.getLogger(__name__)

def send_message(celPhone = '', flow = 1, data = ''):

    part1 = "EAACdvGAiCGEBAJoOBOrvRWpVRjeOQbiTHj5piKOZClPY5Xa8WkCyCOye9mXfZADMEftbjRJbBOI4jJjKXx51Te3oimoh9MMPpErqD5gRZCvO6S6kjq"
    part2 = "7wBEPgBhbrgwZBB1U5CPj8HROOC2hqepguBOyOlwwOeibWectzwhaVs6GYcbgNWV8hmcZA6j4t7hs6jwZAgboTDWmwZDZD"
    idNumber = "100739332996065"
    message = WhatsApp(part1+part2,idNumber)
    celPhone = celPhone.replace("521","52")

    if flow == -1:
        try:
            message.send_button(recipient_id=celPhone, button=welcome())
            return 'Send Message Success'
        except BaseException as error:
            msgLog = error
            logger.error(msgLog)
            return msgLog

    if flow == 0:
        msgToClient = 'Ingresa el número tu de pedido'
        try:
            message.send_message(msgToClient, celPhone)
            return 'Send Message Success'
        except BaseException as error:
            msgLog = error
            logger.error(msgLog)
            return msgLog

    if flow == 1: 
        data = re.sub("[^0-9]", "", data)   
        try:
            pedidos = consultaATG(data)
            if pedidos['noProducts']>0:
                for pedido in pedidos['products']:
                    name = pedido['displayName']
                    numPedido = pedido['pedido']
                    sku = pedido['sku']
                    img = pedido['imgURL']
                    status = pedido['status']
                    message.send_image(
                    image=f'{img}',
                    recipient_id=celPhone,
                    caption = f"""Producto: *{name}*\n\nPedido: *{numPedido}*\n\nCódigo de producto: *{sku}*\n\nEstatus: *{status}*""")
                return 'Send Message Success'
            else:
                msgToClient = 'No existe pedido con el número que me proporcionaste'
                message.send_message(msgToClient, celPhone)
                return 'Send Message Success'
        except BaseException as error:
            msgLog = error
            logger.error(msgLog)
            return msgLog

    if flow == 2:
        msgToClient = 'Estamos abiertos de Lunes a Domingo en un horario de 11:00am a 9:00pm'
        try:
            message.send_message(msgToClient, celPhone)
            return 'Send Message Success'
        except BaseException as error:
            msgLog = error
            logger.error(msgLog)
            return msgLog
    
    if flow == 404:
        msgToClient = 'No entendi tu pregunta'
        try:
            message.send_message(msgToClient, celPhone)
            return 'Send Message Success'
        except BaseException as error:
            msgLog = error
            logger.error(msgLog)
            return msgLog
    
    else:
        msgToClient = 'Aún no cuento con el conocimiento de ese flujo'
        try:
            message.send_message(msgToClient, celPhone)
            return 'Send Message Success'
        except BaseException as error:
            msgLog = error
            logger.error(msgLog)
            return msgLog


# send_message(celPhone = '5215534596395', flow = 1, data = ' es el 1391566978')