import requests
import json

def consultaATG(trNumber):
    try:
        url = "https://pwasso.liverpool.com.mx:8443/rest/model/com/liverpool/OrderSearchActor/orderSearch?trackingNumber="+trNumber #PROD

        payload={}
        headers = {
        'brand': 'LP',
        'channel': 'web',
        'lp-auth-header': 'it8sjpiiDawcbETj8Ls0Qg%3D%3D',
        'Cookie': 'JSESSIONID=!1584890370; genero=x; segment=fuero'
        }

        result = requests.get(url, headers=headers)
        resultjson = json.loads(result.text)
        statusCode=0
        status=""
        noProductos=0
        products=[]
        fecha = ""
        if resultjson["s"]== "0":
            i=0
            CAN = 0 #Cancelado
            ENR = 0
            FFR = 0 #Fecha Fuera de Rango
            FER = 0 #se agrega para escenario donde unos de los SKUs en pedido tiene fecha futura (Fecha En Rango)
            NINV = 0 #No hay inventario disponible
            NHFEE=0 #No hay Fecha Estimada de Entrega
            CC = 0 #producto en click and collect
            PE = 0 #Pedido Entregado
            for field in resultjson.keys():
                if field == "somsOrder":
                    for product in resultjson["somsOrder"]['commerceItems']:
                        i = i+1
                        if "estimatedDeliveryDate" in product.keys():

                            if "EDDErrorCode" in product.keys():
                                error = product["EDDErrorCode"]
                            else:
                                error = ""

                            try:
                                if (("no es posible mostrar la fecha de entrega" in product["estimatedDeliveryDate"] or "no contamos con inventario en bodega" in error.lower()) and product['itemStatus']!='Pedido entregado'):
                                    fecha = " "

                                elif(product['itemStatus']=='Pedido entregado'):
                                    fecha='Pedido entregado'

                                else:
                                    fecha = "Fecha de Entrega: "  + product["estimatedDeliveryDate"]
                                    dates = product["estimatedDeliveryDate"].upper().split("-")
                                    f = dates[len(dates)-1].strip().split(" ")
                                    d=""
                                    x = datetime.now()
                                    if len(f) == 3:
                                        if getMes(f[2]) == "01" and x.month == 12:
                                            d = f[0]+"-"+getMes(f[2])+"-"+str(x.year+1)
                                        else:
                                            d = f[0]+"-"+getMes(f[2])+"-"+str(x.year)
                                    if len(f) == 5:
                                        d = f[0]+"-"+getMes(f[2])+"-"+f[4]
                                    dateFromString = datetime.strptime(d, "%d-%m-%Y")
                                    if "al modulo a recoger" in product["itemStatus"]:
                                        CC = CC+1
                                    if x.date() <= dateFromString.date():
                                        FER = FER+1
                                    else: #se agrega para escenario donde unos de los SKUs en pedido tiene fecha futura (Fecha En Rango)
                                        FFR = FFR+1
                            except:
                                fecha = " "
                        else:
                            NHFEE = NHFEE+1

                        if product["itemStatus"] == "Cancelado":
                            fecha = ""
                        producto = {
                            'pedido':product['pedidoNumber'],
                            'sku':product["SkuId"],
                            'displayName': product["DisplayName"],
                            'imgURL':product["SmallImage"],
                            'estimatedDeliveryDate':fecha,
                            'status':product["itemStatus"]
                        }
                        products.append(producto)
                elif field == "order":
                    for deliveryInfo in resultjson["order"]['deliveryInfo']:
                        for product in deliveryInfo["packedList"]:   
                            if "EDDErrorCode" in product.keys():
                                error = product["EDDErrorCode"]
                            else:
                                error = ""     
                            errors = ["No contamos con inventario en bodega"]               
                            i = i+1
                            # print(product)
                            if ("estimatedDeliveryDate" in product.keys()) and (product['estimatedDeliveryDate'] != None):
                                try:
                                    if (error in errors) or ("no es posible mostrar la fecha de entrega" in product["estimatedDeliveryDate"]): #or not product["estimatedDeliveryDate"]:
                                        fecha = " "
                                        # FFR = FFR+1
                                        NINV = NINV+1
                                    else:                                        
                                        if "Pedido entregado" in product["itemStatus"]:
                                            PE = PE+1

                                        fecha = "Fecha de Entrega: "  + product["estimatedDeliveryDate"]

                                        if deliveryInfo["eddMessage"] != None:
                                            fecha = deliveryInfo["eddMessage"] + " " +fecha

                                        dates = product["estimatedDeliveryDate"].upper().split("-")
                                        f = dates[len(dates)-1].strip().split(" ")
                                        d=""
                                        x = datetime.now()

                                        if len(f) == 3:
                                            if getMes(f[2]) == "01" and x.month == 12:
                                                d = f[0]+"-"+getMes(f[2])+"-"+str(x.year+1)
                                            else:
                                                d = f[0]+"-"+getMes(f[2])+"-"+str(x.year)

                                        if len(f) == 5:
                                            d = f[0]+"-"+getMes(f[2])+"-"+f[4]

                                        dateFromString = datetime.strptime(d, "%d-%m-%Y")

                                        # print(producto['estimatedDeliveryDate'])
                                        # print(fecha)
                                        product['estimatedDeliveryDate']=fecha

                                        if "al modulo a recoger" in product["itemStatus"]: #Clic & collect
                                            CC = CC+1
                                        elif x.date() <= dateFromString.date():
                                            FER = FER+1
                                        else: #se agrega para escenario donde unos de los SKUs en pedido tiene fecha futura (Fecha En Rango)
                                            # FFR = FFR+1
                                            FER+=1
                                except:
                                    fecha = ""
                            elif(product['itemStatus']=='Preparando tu Regalo'):
                                NINV = NINV+1
                            elif(product["itemStatus"] == "Cancelado"):
                                fecha = ""
                                CAN = CAN + 1
                            else:
                                NHFEE = NHFEE+1
                            # if product["itemStatus"] == "Pedido entregado" or product["itemStatus"] == "Regalo Entregado":
                            #     ENR = ENR + 1
                            producto = {
                                'pedido':product['pedidoNumber'],
                                'sku':product["skuID"],
                                'displayName': product["displayName"],
                                'imgURL':product["smallImage"],
                                'estimatedDeliveryDate':fecha,
                                'status':product["itemStatus"]
                            }

                            products.append(producto)
                noProductos=i
        else:
            statusCode=400
            status="NOK"
            noProductos=0
            products=[]
        jsonRaw = {
                'statusCode': 200,
                'noProducts':noProductos,
                'products': products
            }
        return jsonRaw

    except BaseException as error:
        statusCode=401
        status='An exception occurred: {}'.format(error)
        noProductos=0
        products=[]
        jsonRaw = {
                'statusCode': statusCode,
                'status':status,
                'noProducts':noProductos,
                'products': products
            }
        return jsonRaw

# print(consultaATG('1391566978'))